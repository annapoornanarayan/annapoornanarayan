#Write a program to accept strings from the user till user says END.
#Save the data in a text file
#display sentences with begin with upper case letter
myfile=open("text.txt","w")
sentence=""
while True:
    sentence=input("Enter sentence to add or END to exit:")
    if sentence=='END':
        break
    else:
        sentence=sentence+ "\n"
        myfile.write(sentence)
myfile.close()

myfile=open('text.txt','r')
lines=myfile.readlines()
for i in lines:
    if i[0][0].isupper():
        print(i)