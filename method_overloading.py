class Person:
    def detail(self,name:str=None,age:int=None,gender:str=None):
        if(name==None and age==None and gender==None):
            print('None')
        elif(name!=None and age!=None and gender==None):
            print(name,age)
        elif(name!=None and age==None and gender!=None):
            print(name,gender)
        elif(name==None and age!=None and gender!=None):
            print(age,gender)
        else:
            print(name,age,gender)

p1=Person()
p1.detail(18,'male','ragu')