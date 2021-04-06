import argparse

from reader import FileReader, UrlReader
from sma import SMA, SMAPlt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Лабораторная №4')

    parser.add_argument('--paths=', help='Список адресов через запятую',
                        required=True, dest="paths")
    parser.add_argument('--frame=', help='Размер окна',
                        required=True, dest="frame")
    args = parser.parse_args()
    paths = [item for item in args.paths.split(',')]

    if len(paths) < 25:
        print('Кол-во данных меньше 25')
        exit()

    sma = SMA()
    print('Загрузка данных...')
    for path in paths:
        reader = FileReader() if FileReader.path_is_file(path) else UrlReader()
        sma.read_data(reader, path)

    sma.frame = args.frame

    SMAPlt.draw(*sma.calculate_sma())

