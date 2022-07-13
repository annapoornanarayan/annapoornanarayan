# Find if a number is a duck number or not
n=input("Enter number:")
stripped=n.lstrip("0")
if stripped==n:
    print(n, "is not a duck number")
else:
    print(n, "is a duck number")