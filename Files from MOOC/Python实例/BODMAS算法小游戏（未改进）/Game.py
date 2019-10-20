try:
    import ex1 as m

    username = input('Please enter your user name or creat a new name if this is the first time you are running the programe:')
    userscore = int(m.getuserscore(username))

    if userscore == -1:
          newuser = True
          userscore=0
    else:
        newuser=False
        
    userchoice =0
    while userchoice !='-1':
        userscore +=m.generatequestion()
        print("Current Score = ",userscore)
        userchoice = input("Press Enter To Continue or -1 to Exit:")

    m.updateuserpoints(newuser,username,str(userscore))

except Exception as e:
        print("An unexpected error occurred.Program will be exited.")


     
         
    
