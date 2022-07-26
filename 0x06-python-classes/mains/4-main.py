class calculator():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    

    def add(self):
       print (self.num1 +self.num2)

    def subtract(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

def main ():

    oper1 = calculator(12,10)

    oper1.add()

