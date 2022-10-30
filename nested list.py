list1=[]
no_of_students=int(input('enter the number of students:'))
for i in range (no_of_students):
    for j in range(1):
        list2=[]
        name=input('enter the student name:')
        mark=float(input('enter the student mark:'))
        list2.append(name)
        list2.append(mark)
    list1.append(list2)
print(list1)
list1.sort(key = lambda x: x[1])
print(list1)
list3=[]
for i in range(0,len(list1)):
   if(list1[0][1]==list1[1][1]):
        if(list1[i][1]==list1[][]):
list3.sort()
for i in list3:
    print(i)








