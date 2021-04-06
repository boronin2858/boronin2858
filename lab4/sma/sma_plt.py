import os

import matplotlib.pyplot as plt

CHART_FILE_NAME = 'chart.png'
CHART_PATH = f"{os.getcwd()}/{CHART_FILE_NAME}"


class SMAPlt:
    '''Строитель графиков'''
    @staticmethod
    def draw(data, sma_data):
        '''Отрисовать график'''
        plt.plot(range(len(sma_data)), sma_data, range(len(data)), data)
        plt.ylabel('Y')
        plt.xlabel('X')
        plt.savefig(CHART_PATH)
        print(f"Для просмотра графика откройте файл: {CHART_PATH}")
