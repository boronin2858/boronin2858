from calculator import Calculator


print("Для выхода нажмите Ctrl + C")
try:
    x = input("Введите первое число: ")
    while True:
        y = input("Введите второе число: ")
        try:
            calc = Calculator(float(x), float(y))
        except ValueError:
            print("Неверный ввод")
        else:
            operation = input("Операция (+,-,*,/): ")
            if operation == "+":
                res = calc.addition()
            elif operation == "-":
                res = calc.subtraction()
            elif operation == "*":
                res = calc.multiplication()
            elif operation == "/":
                try:
                    res = calc.division()
                except ZeroDivisionError:
                    print("Произошло деление на 0")
                    continue
            print(f"{x}{operation}{y}={res}")

except KeyboardInterrupt:
    pass
