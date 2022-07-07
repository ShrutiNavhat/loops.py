i=1
a=int(input("enter the number :"))
while i==1:
    if a==2 or a==3 or a==5 or a==7:
        print(a,"it is prime number")
    elif a%2!=0 and  a%3!=0 and a%5!=0 and a%7!=0:
        print(a,"it is prime number")
    else:
        print(a,"it is not prime number")
    i=i+1


# i=5
# while i>0:
#     l=5
#     while l>0:
#         print(i,end=" ")
#         l=l-1
#     i=i-1
#     print()



# a=input("enter the word :")
# i=1
# while i==1:
#     print(a)
#     i=i+1



# a=2
# b=11
# c=2003
# print(a,"/",b,"/",c)

# a=(input("enter the number"))
# b=str(a)
# i=0
# while i<len(b):
#     if b[i]=="0":
#         print("Zero")        
         
#     i=i+1    


# list1=[[2,3,45],[7,6,8],[4,6,4]]
# list2=[[2,4,8],[6,5,7,8],[5,9,6,3]]
# i=0
# list3=[]
# while i<len(list1):
#     a=list1[i]+list2[i]
#     list3.append(a)
#     i=i+1
# print(list3)   


# list=[[0,3],[1,3,6],[5,7,4],[4,6,7,8]]
# i=0
# max=list[i]
# min=list[i]
# while i<len(list):
#     if len(list[i])>len(max):
#         max=list[i]
#     if len(list[i])<len(min):
#         min=list[i]
#     i=i+1   
# print((len(max),max))
# print((len(min),min))        
    

# a=["45kb","46hi"]
# i=0
# p=[]
# while i<len(a):
#     if type(a[i][j])==int:
#      j=0
#      while j<len(a[i]):
#         #  if type(a[i][j])==int:
#           p.append(a[i][j])
#         #   print(p)
#           j=j+1    
#     i=i+1        

# list=[[2,4],[5,7],[7,8]]
# sum=0
# i=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         sum=sum+list[i][j]

#         j=j+1
#     i=i+1
# print(sum)        


# list=[[2,4],[5,7],[7,8]]
# i=0
# h=[]
# while i<len(list):
#     j=0
#     sum=0
#     while j<len(list[i]):
#         sum=sum+list[i][j]
#         j=j+1
#     h.append(sum)
#     i=i+1
# print(h)      


# list=[[1,2],[5,6],[7,8]]
# i=0
# p=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         d=list[i][0]
#         j=j+1
#     p.append(d)
#     i=i+1
# print(p)

# f


# l=[1,2,[5,7],6,[3,2,7]]
# i=0
# sum=0
# while i<len(l):
#     if type (l[i])==list:
#         j=0
#         while j<len(l[i]):
#         # if l[i]==list:
#             sum=sum+(l[i][j])
#             j=j+1
#     else:
#             sum=sum+l[i]
#             # j=j+1
#     i=i+1
# print(sum)                 