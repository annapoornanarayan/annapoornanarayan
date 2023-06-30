
def updateSql(uname,won,level):

    import mysql.connector
    db = mysql.connector.connect(host='localhost',
                                 database='bdata',
                                 user='root',
                                 password='Annapoorna@2004')

    mycursor = db.cursor()
    if won==True:
        if level=='1':
            mycursor.execute("update player_set set wins=wins+1,games=games+1,points=points+2 where username='%s'"% (uname,))
        elif level =='2':
            mycursor.execute("update player_set set wins=wins+1,games=games+1,points=points+5 where username='%s'"% (uname,))
            
    else:
        mycursor.execute("update player_set set games=games+1 where username='%s'" % (uname,))

   
    mycursor.close()
    db.commit()
    db.close()
    return "Your progress has been updated"


def recordDisplay():
    import mysql.connector
    
    #from tabulate import tabulate
    db = mysql.connector.connect(host='localhost',
                                 database='bdata',
                                 user='root',
                                 password='Annapoorna@2004')
    mycursor = db.cursor()
    mycursor.execute("select * from player_set order by points desc")
    myrecords=mycursor.fetchall()
    #print(tabulate(myrecords, headers=['Username', 'Wins','Games','Points'], tablefmt='psql'))
    print('\tUsername \t\t Wins   Games  Points')
    for i in myrecords:
        for j in i:
            if type(j)==str:
                print('|','{:^20}'.format(j),'|',end ='\t')
            else:
                print('|',j,'|', end='\t')
        print()
    '''
    for row in myrecords :
        print(row[0].rstrip(), "\t\t\t", row[1], "\t" ,row[2],"\t", row[3])
    '''
    db.commit()
    mycursor.close()
    db.close()
