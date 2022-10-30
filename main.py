data=10
n=3
if((data & ~(1<<n)) ==0):
    print("off")
else:
    print("on")