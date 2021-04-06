class Poly:
    def __init__(self, values):
        self.values = values

    def _poly_func(self, value):
        '''Получить результат для одного значения'''
        try:
            return 1 / value * 3
        except ZeroDivisionError:
            raise

    def get_result(self):
        '''Получить результат для всех значений'''
        try:
            return sum(self._poly_func(value) for value in self.values)
        except ZeroDivisionError:
            print("Введено недопустимое значение 0")
            exit()
