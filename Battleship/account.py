def account():
    #menu choice 1: Access account
    def password_verification(username,password):
        import pickle
        isVerified=False
        myfile=open("logbook.dat","rb")
        try:
            dic=pickle.load(myfile)
            for key in dic:
                if key==username and dic[key]==password:
                    isVerified=True
                    break
        except EOFError:
            myfile.close()
        return isVerified


    #menu choice 2: create account
    def createAccount(username,password):
        import pickle
        myfile=open("logbook.dat","rb")
        dic=pickle.load(myfile)
        dic[username]=password
        myfile.close()
        myfile=open("logbook.dat","wb")
        pickle.dump(dic,myfile)
        myfile.close()
    
    def updatesql(uname):
        import mysql.connector
        db = mysql.connector.connect(host='localhost',
                                 database='bdata',
                                 user='root',
                                 password='Annapoorna@2004')

        mycursor = db.cursor()
        mycursor.execute("insert into player_set (username, wins, games, points) values ('%s',%d,%d,%d)" % (uname,0,0,0))
        mycursor.close()
        db.commit()
        db.close()

    while True:
        print("Choose one from the below:")
        print("1. Access an already created account")
        print("2. Create a new account")
        menu_choice=input("Enter choice:")
        if menu_choice=='1':
            username=input("Enter your username:")
            password=input("Enter password:")
            verified=password_verification(username, password)
            if verified==True:
                player_name=username
                print("Welcome",player_name)
                return player_name
            else:
                print("Your password or username might have been incorrect. Try again (Remember that these are case sensitive)")
        elif menu_choice=='2':
            new_username=input("Enter your username:")
            new_password=input("Enter password:")
            createAccount(new_username, new_password)
            print("Your account has been successfully created. Login again to start playing")
            updatesql(new_username)
            
        else:
            print("Oops! we didn't get that. Try again")
