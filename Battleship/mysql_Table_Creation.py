import mysql.connector

def codeForCreate():

    db = mysql.connector.connect(host='localhost',
                                 database='bdata',
                                 user='root',
                                 password='Annapoorna@2004')
   
    mycursor = db.cursor()

    mycursor.execute("create table if not exists player_set  (username varchar(50) primary key, wins integer default 0, games integer default 0,points integer default 0 )")

    db.commit()
    mycursor.close()
    db.close()
codeForCreate()
