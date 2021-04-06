from urllib.request import urlopen

from .base_reader import BaseReader


class UrlReader(BaseReader):
    '''Ридер для работы с url'''

    def read(self, url):
        '''Чтение данных'''
        data = self._download_file(url)
        return float(data)

    def _download_file(self, url):
        '''Загрузка файла по url'''
        try:
            return urlopen(url).readline()
        except ValueError:
            raise "Ошибка загрузки файла"

