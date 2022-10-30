l = int(input())
for i in range(l):
    t = int(input())
    s = input()
    v = "aeiou"
    count = 0
    flag = False
    for j in s:
        if j in v:
            count = 0
        else:
            count = count + 1
        if (count >= 4):
            flag = True
    if (flag):
        print("No")
    else:
        print("Yes")
