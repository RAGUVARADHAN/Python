class person:
    def __init__(self,name,age):
        self.name='name'
        self.age=age

    def cond(self):
        if(self.age>18 or self.age==18):
            return self.eligible()
        else:
            return self.not_eligible()

    def eligible(self):
        print(self.name,'is eligible for voting')

    def not_eligible(self):
        print(self.name,'is not eligible for voting')
    class student:
        def prit(self):
            print('hello student')


p1=person('ragu',18)
p1.cond()
stu=person.student()
stu.prit()
