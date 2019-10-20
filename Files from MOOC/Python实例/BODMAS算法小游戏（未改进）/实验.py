from random import randint
from os import remove,rename

def getuserscore(username) :  #获取用户得分
    try:
        input=open ('321.txt','r')
        for line in input:
            content = line.split(',')
            if content[0] == username:
               input.close()
               return content[1]
        input.close()
        return '-1'
    except IOError:   #防止偶然写入而新建文件
                print("\nFile userscores.txt not found. A new file will be created.")
                input= open('321.txt','w')
                input.close()
                return "-1"


def updateuserpoints(newuser,username,score):  #更新用户得分
    if newuser:
        input = open('321.txt','a')
        input.write('\n'+ username + ','+ str(score))
        input.close

    else:
        input = open('321.txt','r+')
        output = open('321.tmp','w')
        for line in input:
            content = line.split(',')
            if content[0] == username:
               content[1] = str(score)
               line = content[0]+','+content[1]+'\n'
        output.write(line)
        input.close()
        output.close()

        remove('321.txt')
        rename('321.tmp','321.txt')

def generatequestion(): #生成问题

    operandlist=[0,0,0,0,0]
    operatorlist=['','','','']
    operatordict={1:'+',2:'-',3:'*',4:'**'}

    #随机数更新operandlist
    for i in range(0,5):
        operandlist[i]=randint(1,9)
    
    #数学符号更新operatorlist
    for i in range(0,4):
        if i>0 and operatorlist[i-1] !='**':
            operator=operatordict[randint(1,4)]
        else:
            operator=operatordict[randint(1,3)]
        operatorlist[i]=operator
        
    questionstring=str(operandlist[0])

    #生成一个数学表达式
    for i in range(1,5):
        questionstring = questionstring+operatorlist[i-1]+str(operandlist[i])

    #计算结果
    result=eval(questionstring)

    #设置用户交互   
    questionstring=questionstring.replace("**","^")#问题转换
    print('\n'+questionstring)     #打印问题
    userresult = input('Answer:')   #获取用户答案

    while 1:
        try:
            if int(userresult) == result:
                print ("So Smart")
                return 1
            else:
                print("Sorry,wrong answer.The correct answer is",answer)
                return 0
        except Exception as e:
            print("You did not enter a number.Please try again")
            userresult = input('Answer:')

username=input('Please enter your user name or creat a new name if this is the first time you are running the programe:')
userscore=int(getuserscore(username))

if userscore==-1:
    newuser=True
    userscore=0
else:
    newuser=False
        
userchoice=0
while userchoice !='-1':
    userscore +=generatequestion()
    print("Current Score = ",userscore)
    userchoice = input("Press Enter To Continue or -1 to Exit:")
updateuserpoints(newuser,username,userscore)





