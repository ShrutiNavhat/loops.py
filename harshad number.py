num=int(input("enter the number : "))
i=1
sum=0
while i==1:
   a=(num//100)%10
   b=(num//10)%10
   c=num%10
   sum=a+b+c
   print(sum)
   if num%sum==0:
      print(num%sum,"it is harshad number")
   else:
       print("it is not harshad number")
   i=i+1






