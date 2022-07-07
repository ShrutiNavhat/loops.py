list=[[2,4,5],2,[6,4,5],[7,6,3]] 
i=0
k=[]
while i<len(list):
    if type(list[i])==list:
        j=0
        while j<len(list[i]):
         k.append(list[i][j])
    
    else:
        k.append(list[i])
        j=j+1
    i=i+1
print(k)            

                          
