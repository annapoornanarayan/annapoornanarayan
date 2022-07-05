# 30: Read and display content of a file from end to beginning
myfile=open("text.txt","r")
strlist=myfile.readlines()
print(strlist)
for i in range(len(strlist)-1,-1,-1):
    myfile.readline()
    print(strlist[i])