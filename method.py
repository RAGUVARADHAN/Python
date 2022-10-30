class calc():
    def __init__(self):
        self.a=int(input('enter the value a:'))
        self.b=int(input('enter the value b:'))
        self.oper=input('enter the operation:')
    def add(self):
        if(self.oper=='add'):
            return self.a + self.b
        return self.sub()
    def sub(self):
        if(self.oper=='sub'):
            return self.a - self.b
        return self.mul()
    def mul(self):
        if(self.oper=='mul'):
            return self.a * self.b
        return self.div()
    def div(self):
        if(self.oper=='div'):
            return self.a / self.b

call=calc()
ans=call.add()
print(ans)

