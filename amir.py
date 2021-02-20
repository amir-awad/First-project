num1 = eval(input())
num2 = eval(input())
flag=True
while num1>0:
    if num1%10 == num2%10:
        num1=num1//10
        flag=True
    else:
        num2=num2//10
        flag=False

if flag:
    print("sub")
else:
    print("not sub")


print("I am amir")