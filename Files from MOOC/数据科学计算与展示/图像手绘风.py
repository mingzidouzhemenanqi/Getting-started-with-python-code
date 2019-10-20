# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 09:22:44 2019

@author: Forry
"""

from PIL import Image
import numpy as np

#get the photo
try:
    #path = input("请输入图片名称：")
    path = r"C:/Users/Forry/Desktop/1.jpg"
    a = np.asarray(Image.open(path).convert('L')).astype('float')
except:
    print("error")

depth = 10 #(0,100)
#get the gradient value of the image grayscale
grad = np.gradient(a)
#Take horizontal and vertical image gradient values
grad_x, grad_y = grad
grad_x = grad_x*depth/100
grad_y = grad_y*depth/100
b = np.sqrt(grad_x**2+grad_y**2+1.)
uni_x = grad_x/b
uni_y = grad_y/b
uni_z = 1./b

#Radiant value of the light angle of the light source
vec_el = np.pi/2.2
#Radiant value of source azimuth
vec_az = np.pi/4
#the effect of the light source on the x axis
dx = np.cos(vec_el)*np.cos(vec_az)
#the effect of the light source on the y axis
dy = np.cos(vec_el)*np.sin(vec_az)
#the effect of the light source on the z axis
dz = np.cos(vec_el)

#light source normalization
c = 255*(dx*uni_x+dy*uni_y+dz*uni_z)
c = c.clip(0,255)

#rebuilt the image
im = Image.fromarray(c.astype('uint8'))
im.save(r"C:/Users/Forry/Desktop/2.jpg")















