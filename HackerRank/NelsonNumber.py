#Check whether a number is a Nelson or not
n=input('Enter number:')
ch=n[0]
for i in n:
    if i==ch:
        isNelson="It is a Nelson"
    else:
        isNelson="It is not a Nelson"
print(isNelson)