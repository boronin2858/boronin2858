class SMA:
    '''Алгоритм SMA'''

    def __init__(self):
        # Входные данные
        self._data = []
        # Результат sma алгоритма
        self._sma_data = []
        # Размер окна
        self._frame = 2

    frame = property()

    @property
    def data_len(self):
        return len(self._data)

    @frame.getter
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        if int(value) > 1 and int(value) < len(self._data):
            self._frame = int(value)
        else:
            print(f"Размер окна равен {self._frame}")

    def push_to_data(self, value):
        '''Добавить значение в список входных данных'''
        self._data.append(value)

    def read_data(self, reader, path):
        '''Чтение данных'''
        value = reader.read(path)
        self.push_to_data(value)

    def calculate_sma(self):
        '''Вычисление sma'''
        self._sma_data = [
            (sum(self._data[i - self._frame: self._frame + (i - self._frame)]) / self._frame)
            if i >= self._frame else None
            for i in range(1, len(self._data) + 1)
        ]

        return (self._data, self._sma_data)
