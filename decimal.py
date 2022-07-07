# a=input("enter the number : ")
# i=0
# while i<len(a):
#     if a[i]==str(1):
#         print("one")
#     elif a[i]==str(2):
#         print("two")
#     elif a[i]==str(3):
#         print("three")
#     elif a[i]==str(4):
#         print("four")
#     elif a[i]==str(5):
#         print("five")
#     elif a[i]==str(6):
#         print("six")
#     elif a[i]==str(7):
#         print("seven")
#     elif a[i]==str(8):
#         print("eight")
#     elif a[i]==str(9):
#         print("nine")
#     elif a[i]==str(10):
#         print("ten")
#     i=i+1
    

# a=str(input("enter the word : "))
# i=1
# for i in a:
#     print(i)



# i=1
# while i<=5:
#     b=5-i
#     while b>0:
#         print("",end="")
#         b=b-1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1

# i=1
# while i<=10:
#     if i==4:
#         break
#     print(i)
#     i=i+1

i=1
while i<=10:
    i=i+1
    if i==4 or i==7:
        continue
    print(i)





# a=int(input("enter the number : "))
# b=int(input("enter the number : "))
# i=a
# count=0
# count1=0
# sum=0
# sum1=0
# while i<=b:
#     if i%2==0:
#         print(i,"even number")
#         count=count+1
#         sum=sum+i
#     else:
#         print(i,"odd number")
#         count1=count1+1
#         sum1+=i
#     i=i+1
# print("count of even numbers =",count)
# print("sum of even numbers =",sum)
# avg=sum/count
# print("avg of even numbers =",avg)
# print("count of odd numbers =",count1)
# print("sum of odd numberes =",sum1)
# avg1=sum1/count1
# print("avg of odd numbers =",avg1)



# a=int(input("enter thr number : "))
# i=1
# while i<=a:
#     j=1
#     while j<=10:
#         print(i,"=",j*i)
#         j=j+1
#     print()
    # i=i+1


# i=0
# a=int(input("enter the number : "))
# x=a
# while a>0:
#     i=(i*10)+a%10
#     a=a//10
# print(i*10)
    
    
    
# i=1
# while i<=3:
#     b=5-i
#     while b>0:
#         print(" ",end=" ")
#         b=b-1
#     a=1
#     while a<=i:
#         print("*",end="")
#         a+=1
#     print()
#     i=i+2
# i=2
# while i>=1:
#     b=5-i
#     while b>0:
#         print(" ",end="")
#         b=b-1
#     a=1
#     while a<=i:
#         print("*",end="")
#         a=a+1
#     print()
#     i=i-2