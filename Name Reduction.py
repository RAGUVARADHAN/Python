from itertools import permutations
t=int(input('number of trail:'))
plist=[]
clist=[]
for i in range(t):
    pname=input('enter the parent name:')
    noc=int(input('enter the noc:'))
    c1=''
    for j in range(noc):
        cname=input('enter the child name:')
        c1=c1+cname
        prem1=permutations(c1)
        prem2=permutations(pname)
        for i in list(prem1):
            ''.join(i)
            clist.append(i)
        for j in list(prem2):
            ''.join(j)
            plist.append(j)
if (set(clist).issubset(plist)):
    print('yes')
else:
    print('No')




