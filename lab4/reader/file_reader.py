import os

from .base_reader import BaseReader


class FileReader(BaseReader):
    '''Ридер для работы с файлами'''

    def read(self, path):
        '''Чтение из файла'''
        if self.path_is_file(path):
            with open(path, 'r') as f:
                try:
                    data = float(f.readline())
                except ValueError:
                    print(f'Введено недопустимое значение: {f.readline()}')
            return data

    @classmethod
    def path_is_file(cls, path):
        '''Проверка существования файла'''
        return os.path.exists(path)

