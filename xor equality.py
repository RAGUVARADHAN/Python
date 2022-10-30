tc=int(input('enter the test case:'))
for i in range(tc):
    N=int(input('enter the num:'))
    count=0
    for x in range(0,(2**N)-1):
        a=x^(x+1)
        b=(x+2)^(x+3)
        if(int(a)==int(b)):
            count+=1
    print(count)
