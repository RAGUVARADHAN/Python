def unique(numbers):
    unique_list=[]
    for i in numbers:
        if(i not in unique_list):
            unique_list.append(i)
    return unique_list
        

print(unique([1,2,3,2,2,3,4,7,6]))



