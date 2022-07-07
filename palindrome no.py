i=0
a=int(input("enter the number : "))
x=a
while a>0:
    i=(i*10)+a%10
    a=a//10
if x==i:
    print(i,"yes")
else:
    print(i,"no")



# # a="computer"
# for i in a:
#     print(i)



# i=0
# a=int(input("enter the number:"))
# x=a
# while a>0:
#     i=(i%10)+a%10
#     a=a//10
# if x==i:
#     print(i,"yes")
# else:
#     print(i,"no")

# i=0
# a=int(input("enter the number:"))
# x=a
# while a>0:
#     i=(i*10)+a%10
#     a=a//10
# if x==i:
#     print(i,"yes")
# else:
#     print(i,"no")




# n=int(input("enter the number:"))
# i=1
# sum=0
# while i<=n:
#     a=n%10
#     b=(n//10)%10
#     c=(n//100)%10
#     a=a**3
#     b=b**3
#     c=c**3
#     sum=a+b+c
#     i=i+1
# if sum==n:
#     print(n,"it is armstrong number")
# else:
#     print(n,"it is not armstrong number")


# n=int(input("enter the number:"))
# i=1
# sum=0
# while i<=n:
#     a=n%10
#     b=(n//10)%10
#     c=(n//100)%10
#     sum=a+b+c
#     i=i+1
# if n%sum==0 :
#     print(n,"harshad")
# else:
#     print(n,"not")


