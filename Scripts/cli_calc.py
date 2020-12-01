import fire

class Calculator:
    def check(self, x, y):
        if ((isinstance(x, int) or isinstance(x, float)) and 
            (isinstance(y, int) or isinstance(y, float))):
            return True
        else:
            return False
    def add(self, x,y):
        if self.check(x,y):
            return x+y
    def subtract(self, x,y):
        if self.check(x,y):
            return x-y
    def multiply(self, x,y):
        if self.check(x,y):
            return x*y
    def divide(self, x,y):
        if self.check(x,y):
            return x/y

# temp = Calculator()
# print(temp.add(3,4))
# print(temp.subtract(3,4))
# print(temp.multiply(3,4))
# print(temp.divide(3,4))

if __name__ == '__main__':
    fire.Fire(Calculator)
