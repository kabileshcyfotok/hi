# conditional statement
a=int(input("Enter a value of a:"))
b=int(input("Enter a value of b:"))
c=int(input("Enter a value of c:"))
if a<b and a<c :
    print(f"{a} is Smaller")
elif b<c:
    print(f"{b} is Smaller")
else:
    print(f"{c} is Smaller")