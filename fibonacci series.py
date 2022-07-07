num=int(input("enter number:"))
a=0
b=1
count=0
while count<num:
    if count==0:
        print(0)
    print(b)
    a,b=b,a+b
    count=count+1


