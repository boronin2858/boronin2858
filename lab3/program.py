import argparse

from poly import Poly


class Program:

    def __init__(self):
        parser = argparse.ArgumentParser(description='Лабораторная №3')
        parser.add_argument('--poly=', action="store", required=True,
                            dest="poly", help="Список значение, через запятую")

        self.args = parser.parse_args()

    def _get_input_values(self):
        '''Получение введенных значений'''
        values=[]
        for val in self.args.poly.split(','):
            try:
                values.append(float(val))
            except ValueError:
                print(f"Введено недопустимое значение: {val}")
                exit()
                
        return values

    def get_poly_result(self):
        '''Получение результата выполнения полинома'''
        values = self._get_input_values()
        poly = Poly(values)
        return poly.get_result()

