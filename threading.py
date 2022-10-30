from threading import *
def hi():
    for i in range(5):
        print('hi',current_thread().getName())
t1=Thread(target=hi)
t1.start()