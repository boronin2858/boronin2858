import os

import matplotlib.pyplot as plt

CHART_FILE_NAME = "chart.png"
CHART_PATH = f"{os.getcwd()}/{CHART_FILE_NAME}"


class BarGraph:
    '''Строитель гистрограмм'''
    @staticmethod
    def draw(stat):
        '''Построение гистограммы'''
        print('Рисуем график')
        authors = []
        messages = []
        for author, stat in stat.items():
            authors.append(author)
            messages.append(stat['messages'])

        fig, ax = plt.subplots()

        # строим столбцы
        ax.bar(range(len(messages)), messages)
        #  Устанавливаем позиции
        ax.set_xticks(range(len(messages)))
        #  Устанавливаем подписи
        ax.set_xticklabels(authors, rotation=90)

        fig.set_figwidth(len(authors))
        fig.set_figheight(30)

        plt.savefig(CHART_PATH)
        print(f"Для просмотра графика откройте файл: {CHART_PATH}")
