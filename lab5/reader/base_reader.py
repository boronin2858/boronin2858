from abc import ABC, abstractmethod


class BaseReader(ABC):
    '''Базовый ридер'''
    @abstractmethod
    def read(self, path):
        pass
