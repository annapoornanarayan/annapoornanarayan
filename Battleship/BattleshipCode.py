print('\t                            BATTLESHIP')
print("Pick to play against the clock through lives in level 1 or against the computer in level 2")
a='begin'
while a=='begin':
  choose=input("ENTER LEVEL(1 or 2):")
  if choose=='1':
    print("/"*80)
    print("-"*35,"LEVEL 1","-"*40)
    print("Enter the x and y coordinates of where you think the ship is.")
    print("Enter the x coordinate which is from 0 to 4, press enter and then input the y coordinate from 0 to 4")
    print("\t                      You have 5 lives")
    print("\t                        ALL THE BEST!")
    print('/'*80)

    import random
    x = (random.randint(0, 4))
    y = (random.randint(0, 4))
    lives = 5
    row = ['o']
    board = []

    for i in range(0, 5):
        board.append(row * 5)


    def board_display():
        for j in board:
            seperator = " "
            print(seperator.join(j))


    def reply():
        board[4 - y_input][x_input] = "x"
        board_display()
        print("Lives left:", lives)

    def hint_x():
      if x<x_input:
        print("HINT:x coordinate is SMALLER")
      elif x>x_input:
        print("HINT:x coordinate is LARGER")
    def hint_y():
      if y<y_input:
        print("HINT:y coordinate is SMALLER")
      elif y>y_input:
        print("HINT:y coordinate is LARGER")
    #x coordinate==column number
    #y coordinate==row number

    board_display()
    x_input = int(input("Enter x coordinate:"))
    y_input = int(input("Enter y coordinate:"))
    while lives > 0:
        lives = lives - 1
        if x_input == x and y_input == y:
            print("You've sunk the battleship! You have won! GAME OVER")
            board[4 - y_input][x_input] = "*"
            board_display()
            break

        elif x_input > 4 or x_input < 0 or y_input > 4 or y_input < 0:
            print("You have landed outide the battle field.TRY AGAIN")
            board_display()
            x_input = int(input("Enter x coordinate:"))
            y_input = int(input("Enter y coordinate:"))

        elif x_input == x and y_input != y:
            print("The x coordinate is correct, but y is incorrect......")
            hint_y()
            reply()
            if lives>0:
              y_input = int(input("Enter y coordinate:"))
        elif x_input != x and y_input == y:
            print("The y coordinate is correct, but x is incorrect......")
            hint_x()
            reply()
            if lives>0:
              x_input = int(input("Enter x coordinate:"))

        elif x_input != x and y_input != y:
            print("Wrong answer!")
            hint_x()
            hint_y()
            reply()
            if lives>0:
              x_input = int(input("Enter x coordinate:"))
              y_input = int(input("Enter y coordinate:"))
              

    else:
        print("Your lives are used up! You have lost. GAME OVER")


  if choose=='2':
      print()
      print("\t                        BATTLESHIP")
      print("/"*80)
      print("-"*35,"LEVEL 2","-"*40)
      print("Enter the x and y coordinates of the location of your battleship.")
      print("Enter the x coordinate which is from 0 to 4, press enter and then input the y coordinate from 0 to 4 of the location where you think the battleship of the opponent is.")
      print("\t You must sink your opponent's battleship before they guess yours ")
      print("\t                        ALL THE BEST!")
      print('/'*80)

      listx=[0,1,2,3,4]
      listy=[0,1,2,3,4]   

      new_board = []

      for i in range(0, 5):
        new_board.append(['O' ]* 5)
      def my_board():
        for j in new_board:
            seperator = " "
            print('\t'*10,seperator.join(j))
      my_board()
      my_x=int(input("Enter my x coordinate:"))
      my_y=int(input("Enter my y coordinate:"))
      if my_x<=4 and my_x>=0 and my_y>=0 and my_y<=4:
        print("You have located your battleship at:")
        new_board[4-my_y][my_x]="*" 
        my_board()
        print()
        passed=1

      else:
        print("Battleship location is not valid. Try again")
        passed=3
      import random
      x = (random.randint(0, 4))
      y = (random.randint(0, 4))
      lives = 5
      row = ['o']
      board = []

      for i in range(0, 5):
          board.append(row * 5)


      def board_display():
          for j in board:
              seperator = " "
              print(seperator.join(j))


      def reply():
          board[4 - y_input][x_input] = "x"
          board_display()
      def replace():
          new_board[4 - guessy][guessx] = "X"
          my_board()

      def hint_x():
        if x<x_input:
          print("HINT:x coordinate is SMALLER")
        elif x>x_input:
          print("HINT:x coordinate is LARGER")
      def hint_y():
        if y<y_input:
          print("HINT:y coordinate is SMALLER")
        elif y>y_input:
          print("HINT:y coordinate is LARGER")
      #x coordinate==column number
      #y coordinate==row number



      while passed<2:
        while passed==1:
            print("Your turn to guess the location of your opponent's battleship")
            board_display()
            x_input = int(input("Enter x coordinate:"))
            y_input = int(input("Enter y coordinate:"))
            if x_input == x and y_input == y:
                print("You've sunk the battleship! You have won! GAME OVER")
                board[4 - y_input][x_input] = "*"
                board_display()
                passed=3
                break

            elif x_input > 4 or x_input < 0 or y_input > 4 or y_input < 0:
                print("You have landed outide the battle field.TRY AGAIN")

            elif x_input == x and y_input != y:
                print("The x coordinate is correct, but y is incorrect......")
                hint_y()
                passed=0
                reply()

            elif x_input != x and y_input == y:
                print("The y coordinate is correct, but x is incorrect......")
                hint_x()
                passed=0
                reply()

            elif x_input != x and y_input != y:
                print("Wrong answer!")
                hint_x()
                hint_y()
                passed=0
                reply()
            
            else:
              print("Coordinate not valid. TRY AGAIN")
      
        while passed==0:
          a=random.randrange(0,len(listx))
          b=random.randrange(0,len(listy))
          guessx=listx[a]
          guessy=listy[b]
          print("\t"*5,"Opponent has guessed:", "(",guessx,",",guessy,")")
          if guessx == my_x and guessy == my_y:
                print("\t"*5,"The opponent has sunk the battleship! You have lost! GAME OVER")
                board[4 - guessy][guessx] = "*"
                my_board()
                passed=3
                break

          elif guessx == my_x and guessy !=my_y:
                print("\t"*5,"The opponent has guessed the correct x coordinate but the incorrect y coordinate.")
                replace()
                listx=[guessx]
                passed=1
                if guessy<my_y:
                  for ch in listy:
                    if ch<=guessy:
                      listy.remove(ch)
                elif guessy>my_y:
                  for chh in listy:
                    if chh>=guessy:
                      listy.remove(chh)
                
              

          elif guessx != my_x and guessy == my_y:
                print("\t"*5,"The opponent has guessed the correct y coordinate but the incorrect x coordinate.")
                #hint_x()
                replace()
                listy=[guessy]
                passed=1
                if guessx<my_x:
                  for hc in listx:
                    if hc<=guessx:
                      listx.remove(hc)
                elif guessx>my_x:
                  for hcc in listx:
                    if hcc>=guessx:
                      listx.remove(hcc)
              

          elif guessx != my_x and guessy != my_y:
              print("\t"*5,"The opponent has not gotten the correct coordinate.")
              replace()
              passed=1
              if guessy<my_y:
                for ch in listy:
                  if ch<=guessy:
                    listy.remove(ch)
              if guessy>my_y:
                for chh in listy:
                  if chh>=guessy:
                    listy.remove(chh)
              if guessx<my_x:
                for hc in listx:
                  if hc<=guessx:
                    listx.remove(hc)
              if guessx>my_x:
                for hcc in listx:
                  if hcc>=guessx:
                    listx.remove(hcc)
              
      if passed==3:
          print("---------------------GAME OVER------------------------")


  elif choose!='1' and choose!='2':
        print('Not valid!')
