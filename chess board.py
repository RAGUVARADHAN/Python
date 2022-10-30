trail=int(input('enter the trail:'))
def chess():
    for i in range(trail):
        n = int(input('enter the chessboard size:'))
        count = 0
        for j in range(1,n+1,2):
            k=n-j+1
            count+=(k*k)
        print(count)
chess()

