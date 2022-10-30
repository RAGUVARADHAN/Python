x=int(input())
lst=[]
for i in range(x):
    name = input()
    score = float(input())
    lst1=[]
    lst1.append(name)
    lst1.append(score)
    for j in range(1):
        lst.append(lst1)
x = lst[0][1]
y=lst[0][0]
for i in range(len(lst)):
    if(x<lst[i][1]):
        x=lst[i][1]
        y=lst[i][0]
z=lst[0][1]
a=lst[0][0]
for i in range(len(lst)):
    if(x==lst[i][1]):
        z=lst[i][1]
        a=lst[i][0]
        print(a)







