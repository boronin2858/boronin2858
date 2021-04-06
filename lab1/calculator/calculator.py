class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        '''Сложение'''
        return self.x + self.y

    def multiplication(self):
        '''Умножение'''
        return self.x * self.y

    def subtraction(self):
        '''Вычитание'''
        return self.x - self.y

    def division(self):
        '''Деление'''
        return self.x / self.y
