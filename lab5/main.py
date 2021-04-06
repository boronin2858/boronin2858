import argparse

from analyzer import Analyzer
from chart import BarGraph
from reader import FileReader

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Лабораторная №5')
    parser.add_argument('--path=', action="store", required=True,
                        dest="path", help="путь до файла")
    args = parser.parse_args()

    data = FileReader.read(args.path)

    analyzer = Analyzer(data)
    spammers = analyzer.spammer_list
    if not spammers:
        print('Спамеры не обнаружены')
    else:
        print('Список спамеров:')
        for spammer in spammers:
            print(spammer)

    BarGraph.draw(analyzer.info)
