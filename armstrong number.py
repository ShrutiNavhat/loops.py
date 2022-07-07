num=int(input("enter the number : "))
i=1
sum=0
while i<=1:
    a=num%10
    b=(num//10)%10
    c=(num//100)%10
    a=a**3
    b= b**3
    c= c**3
    i=i+1
    sum=a+b+c
if sum==num:
    print(sum,"it is armstrong number")
else:
    print(sum,"it is not armstrong number")

# num=int(input("enter the number : "))
# i=1
# sum=0
# while i<=1:
#     a=num%10
#     b=(num//10)%10
#     c=(num//100)%10
#     a=a**3
#     b=b**3
#     c=c**3
#     i=i+1
#     sum=a+b+c
# if sum==num:
#     print(sum,"it is armstrong number ")
# else:
#     print(sum,"it is not armstrong number ")




