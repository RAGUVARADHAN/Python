tc=int(input('enter the test case:'))
for i in range(tc):
    a,b=map(int,input('enter the total num and the total swap:').split())
    num=list(map(int,input('enter the num:').split()))
    j,k,result1,result2=0,1,0,0
    if(b!=0):
        for i in range(b):
            ini,fin=map(int,input('enter the swapping place:').split())
            num[ini],num[fin]=num[fin],num[ini]
    while j<len(num):
        result1=num[j]+result1
        j+=2
    while k<len(num):
        result2=num[k]+result2
        k+=2
    if(result1<result2):
        print('Tomu wins the game with {} points'.format(result2))
    else:
        print('Motu wins the game with {} points'.format(result1))




