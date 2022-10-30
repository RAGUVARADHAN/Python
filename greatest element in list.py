list_1=[]
x=int(input('enter the no of elements:'))
for i in range(x):
    y=eval(input('enter the value:'))
    list_1.append(y)
a=list_1[0]
for b in list_1:
    if(b>a):
        a=b
print('the largest number is:',a)
            
    
        
        





