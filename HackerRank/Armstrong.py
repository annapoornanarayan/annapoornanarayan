#Write a program to check if the number is Armstrong or not
# sum of cubes of digits is equal to number itself
num=input("Enter number:")
summ=0
for i in num:
    summ=summ+int(i)**3
if summ==int(num):
    print("It is an armstrong number")
else:
    print("It is NOT an armstrong number")