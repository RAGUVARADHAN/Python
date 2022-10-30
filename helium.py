def helium():
    for i in range(z):
        a, b, x, y = map(int, input('enter the a,b,x,y value:').split()) #a and b are required amount x and y are given amount
        c = a * b
        d = x * y
        if (c < d or c == d):
            print('Yes')
        else:
            print('No')

z=int(input('Tell me the no. of trails:'))
helium()
