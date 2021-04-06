import os
import re
from itertools import groupby

from .base_reader import BaseReader


class FileReader(BaseReader):
    '''Ридер файлов'''
    @classmethod
    def read(cls, path):
        '''Чтение данных из файла'''
        if not FileReader.path_is_file(path):
            raise 'Файл не найден'

        print('Чтение файла')
        with open(path, 'r') as f:
            # читаем файл по регулярке
            documents = re.findall(r"(.*?)\n----------------------\n", f.read(), re.DOTALL)

        # вытаскиваем Author, X-DSPAM-Confidence, X-DSPAM-Probability
        documents = [
            {
                'Author': re.search(r'Author: .*', document)
                            .group(0)
                            .split(' ')[1],
                'X-DSPAM-Confidence': re.search(r'X-DSPAM-Confidence: .*', document)
                                        .group(0)
                                        .split(' ')[1],
                'X-DSPAM-Probability': re.search(r'X-DSPAM-Probability: .*', document)
                                        .group(0)
                                        .split(' ')[1]
            }
            for document in documents
        ]
        print('Чтение закончено')
        # группируем все записи по Author
        return groupby(documents, lambda document: document['Author'])

    @classmethod
    def path_is_file(cls, path):
        '''Проверка существования файла'''
        return os.path.exists(path)
