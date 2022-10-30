def shop(x,tot):
    for i in range(x):
        amt=int(input('enter the price:'))
        if(tot>amt or tot==amt):
            rem=tot-amt
            print('Remaining:',rem)
        else:
            print('not enough money')
x=int(input('no of items:'))
tot=int(input('enter the total you have:'))
shop(x,tot)
print('Thank u come again...')

