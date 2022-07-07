i=1
while i<=100:
    print(i)
    i=i+1

i=1
sum=0
while i<=100:
    sum=sum+i
    print(i)
    i=i+1
print(sum)

i=1
sum=0
while i<=10:
    if i%2==0:
        print(-i)
    else:
        print(i)
    i=i+1

    

i=1
sum=0
while i<=100:
    if i%2==0:
        print(i)
        sum=sum+i
    i=i+1
print(sum)


i=0
while i<=9:
  i=i+1
  if i==5:
   continue
print(i)
i=1
while i<=5:
    a=int(input("enter the number : "))
    if a>0:
        print("positive number")
    elif a<0:
        print("negative number")
    else:
        print("zero")
    i=i+1



i=1
sum=0
while i<=10:
    a=int(input("enter the number : "))
    sum=sum+a
    i=i+1
print(sum)