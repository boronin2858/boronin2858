class SQRT:

    def __call__(self, value):
        if value < 0:
            raise ValueError('math domain error')

        # изменение точности от числа
        self.accuracy = 10**-10 if value < 100000 else 10**-6

        # стартовое приближение
        approximation = 1.0

        # поиск корня по формуле Герона
        while not self._check(value, approximation):
            approximation = self._iter(value, approximation)

        return approximation if approximation % 1 > 0.001 else approximation // 1

    def _iter(self, value, approximation):
        '''Итерация вычисления квадратного корня'''
        return 0.5 * (approximation + value / approximation)

    def _check(self, value, approximation):
        '''Проверка точности числа методом Ньютона'''
        if abs(value - approximation**2) < self.accuracy:
            return 1
        return 0
