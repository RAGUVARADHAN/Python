tc=int(input('enter the test case:'))
nop=int(input('enter the no of pile:'))
for i in range(tc):
    list1=list(map(int,input('enter the number of stones in each pile:').split()))
    x=list1[0]
    y=0
    for k in list1:
        if(k>y):
            y=k
    print(y+x)
