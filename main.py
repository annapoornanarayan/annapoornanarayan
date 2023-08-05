from functions import view_Budget
from functions import view_Income
from functions import view_Expense
while True:
  print("Welcome to Budgeter")
  
  print("Enter your desired operation:")
  
  print("1. View Graph")
  print("2. View Budget Table")
  print("3. View Income Table")
  print("4. View Expense Table")
  print("5. Add entry (earning, expense or investment")
  print("6. Quit")
  
  choose=int(input("Enter choice:"))
  if choose==1:
    pass
  elif choose==2:
    view_Budget()
  elif choose==3:
    view_Income()
  elif choose==4:
    view_Expense()
  elif choose==5:
    pass
  elif choose==6:
    break
  else:
    print("Invalid input, try again")
  