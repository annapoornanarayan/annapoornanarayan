def view_Income():
  import mysql.connector
  db=mysql.connector.connect(host='localhost', user='root', password="*******",database='budget')
  mycursor=db.cursor()

  yr=int(input("Enter the year required:"))
  mn=input("Enter month in mmm format:")
  #mycursor.execute("insert into Income (username, wins, games, points) values ('%s',%d,%d,%d)" % (uname,0,0,0))
 
  mycursor.execute("select title,amount from Income where year=%d and month='%s' order by year desc;" % (yr, mn))
  myrecords=mycursor.fetchall()
  print('Income sources for ', mn, " ",yr, " are:")
  print("Title", "\tAmount")
  for i in myrecords:
      for j in i:
          print(j, end=" |")
      print()
    
  mycursor.close()
  db.commit()
  db.close()

def view_Expense():
  import mysql.connector
  db=mysql.connector.connect(host='localhost', user='root', password="**********",database='budget')
  mycursor=db.cursor()

  yr=int(input("Enter the year required:"))
  mn=input("Enter month in mmm format:")
  #mycursor.execute("insert into Income (username, wins, games, points) values ('%s',%d,%d,%d)" % (uname,0,0,0))
 
  mycursor.execute("select title,amount from Expense where year=%d and month='%s' order by year desc;" % (yr, mn))
  myrecords=mycursor.fetchall()
  print('Expenditure sources for ', mn, " ",yr, " are:")
  print("Title", "\tAmount")
  for i in myrecords:
      for j in i:
          print(j, end=" |")
      print()
    
  mycursor.close()
  db.commit()
  db.close()



def view_Budget():
  import mysql.connector
  db=mysql.connector.connect(host='localhost', user='root', password="************",database='budget')
  mycursor=db.cursor()
  mycursor.execute("select * from budget;")
  myrecords=mycursor.fetchall()
  
  print("Year\tMonth     Net Income| Net Expense| Savings")
  for i in myrecords:
      for j in i:
          print(j,"\t" ,end=" ")
          if type(j)==str:
              print("  ", end="  ")
      print()
  mycursor.close()
  db.close()
  
def update_Budget(yr,mn):
      import mysql.connector
      db=mysql.connector.connect(host='localhost', user='root', password="************",database='budget')
      mycursor=db.cursor()
      try:
          mycursor.execute("Select sum(amount) from Income where year=%d and month='%s'" % (yr,mn))
          my_i_data=mycursor.fetchall()
          net_income=my_i_data[0][0]
          
          mycursor.execute("Select sum(amount) from Expense where year=%d and month='%s'" % (yr,mn))
          my_e_data=mycursor.fetchall()
          net_expense=my_e_data[0][0]

          mycursor.execute("Update budget set Net_Income=%d, Net_Expense=%d, Net_Savings=Net_Income-Net_Expense where Year=%d and Month='%s';" % (net_income,net_expense,yr,mn))
      except:
          mycursor.execute("Insert into budget values (%d, '%s', 0, 0, 0);"%(yr,mn))
      
      mycursor.close()
      db.commit()
      db.close()
      
def add_income():
      import mysql.connector
      db=mysql.connector.connect(host='localhost', user='root', password="**********",database='budget')
      mycursor=db.cursor()
      
      year=int(input("Enter year of income:"))
      month=input("Enter month of income in mmm format:")
      title=input("Enter a short title describing the source of income:")
      amount=float(input("Enter the amount of income:"))

      mycursor.execute("insert into income values (%d,'%s','%s',%d);" % (year,month,title,amount))

      mycursor.close()
      db.commit()
      db.close()

      update_Budget(year,month)

def add_expense():
      import mysql.connector
      db=mysql.connector.connect(host='localhost', user='root', password="***********",database='budget')
      mycursor=db.cursor()
      
      year=int(input("Enter year of expense:"))
      month=input("Enter month of expense in mmm format:")
      title=input("Enter a short title describing the reason for expense:")
      amount=float(input("Enter the amount spent:"))

      mycursor.execute("insert into expense values (%d,'%s','%s',%d);" % (year,month,title,amount))

      mycursor.close()
      db.commit()
      db.close()

      update_Budget(year,month)

def remove_income():
      import mysql.connector
      db=mysql.connector.connect(host='localhost', user='root', password="***********",database='budget')
      mycursor=db.cursor()
      
      year=int(input("Enter year of income:"))
      month=input("Enter month of income in mmm format:")
      title=input("Enter the title:")
     
      try:
          mycursor.execute("delete from income where year=%d and month='%s' and title='%s');" % (year,month,title))
          mycursor.close()
          db.commit()
          db.close()

          update_Budget(year,month)
      except:
          print("Not found")

      
def remove_expense():
      import mysql.connector
      db=mysql.connector.connect(host='localhost', user='root', password="********",database='budget')
      mycursor=db.cursor()
      
      year=int(input("Enter year of expense:"))
      month=input("Enter month of expense in mmm format:")
      title=input("Enter the title:")
     
      try:
          mycursor.execute("delete from expense where year=%d and month='%s' and title='%s');" % (year,month,title))
          mycursor.close()
          db.commit()
          db.close()

          update_Budget(year,month)
      except:
          print("Not found")

