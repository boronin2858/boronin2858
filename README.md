# Лабораторные работы

###### OS: Linux
###### Language: Python3

## Запуск проекта

* Перейти в директорию с проектами 
```sh
cd [путь_до_папки]/labs
```
* Создать виртуальное окружение
```sh
python3 -m venv env
```
* Активировать виртуальное окружение
```sh
. env/bin/activate
```
* Произвести установку дополнительных пакетов
```sh
pip install -r requirements.txt
```
## Лабораторная №[1, 2]
* Активировать виртуальное окружение (если не активировано)
```sh
. env/bin/activate
```
* Перейти в директорию с программой
```sh
cd [путь_до_папки]/labs/lab[1,2]
```
* Запустить программу
```sh
python3 main.py
```
## Лабораторная №3
* Активировать виртуальное окружение (если не активировано)
```sh
. env/bin/activate
```
* Перейти в директорию с программой
```sh
cd [путь_до_папки]/labs/lab3
```
* Запустить программу
```sh
python3 main.py --poly=1,2,3,4,5,6,7,8,9,10
```

## Лабораторная №4
* Активировать виртуальное окружение (если не активировано)
```sh
. env/bin/activate
```
* Перейти в директорию с программой
```sh
cd [путь_до_папки]/labs/lab4
```
* Запустить программу
```sh
python3 main.py --frame=5 --paths=data/1.txt,data/2.txt,data/3.txt,data/4.txt,data/5.txt,data/6.txt,data/7.txt,data/8.txt,data/9.txt,data/10.txt,data/11.txt,data/12.txt,data/13.txt,data/14.txt,data/15.txt,data/16.txt,data/17.txt,data/18.txt,data/19.txt,data/20.txt,data/21.txt,data/22.txt,data/23.txt,https://dropmefiles.com.ua/en/d/4zELaZmS3x/02ff9da844ffbab5c01c0cd06386b958/d2ddea18f00665ce8623e36bd4e3c7c5,https://dropmefiles.com.ua/en/d/4zELaZmS3x/02ff9da844ffbab5c01c0cd06386b958/54229abfcfa5649e7003b83dd4755294
```
* Программа выведет путь до файла с графиком

## Лабораторная №5
* Тестовые файлы уже находятся в директории с лаборатоной работой
* Активировать виртуальное окружение (если не активировано)
```sh
. env/bin/activate
```
* Перейти в директорию с программой
```sh
cd [путь_до_папки]/labs/lab5
```
* Запустить программу для маленького файла
```sh
python3 main.py --path=mbox_small.txt
```
* Запустить программу для большого файла
```sh
python3 main.py --path=mbox.txt
```
* Программа выведет путь до файла с гистрограммы и список спамеров, если он есть
