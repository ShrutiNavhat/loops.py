# i=0
# a=int(input("enter the number : "))
# while a>=1:
#     i=(i*10)+a%10
#     a=a//10
#     # b=a%10
#     if a==1 or i==1 :
#         print("one")
#     elif a==2 or i==2 :
#         print("two")
#     elif a==3 or i==3:
#         print("three")
#     elif a==4 and i==4:
#         print("four")
#     elif a==5 or i==5:
#         print("five")
#     elif a==6 or i==6:
#         print("six")
#     elif a==7 or i==7:
#         print("seven")
#     elif a==8 or i==8:
#         print("eight")
#     elif a==9 or i==9:
#         print("nine")
#     i=i+1
# print(a)



i=0
a=int(input("enter the number : "))
x=a
while a>0:
    i=(i*10)+a%10
    a=a//10
print(i*10)