#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from routes import *

if __name__ == '__main__':
    routes = []
    while True:
        print("""
        1. Добавить маршрут
        2. Вывести список маршрутов
        3. Найти маршрут по номеру
        4. Выйти
        """)

        choice = int(input("Выберите пункт меню: "))
        if choice == 1:
            add_route(routes)
        elif choice == 2:
            print_route(routes)
        elif choice == 3:
            get_route(routes)
        elif choice == 4:
            break
        else:
            print("Неверный пункт меню. Попробуйте еще раз.")
