#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils

if __name__ == '__main__':
    # получаем функцию get_min_or_max из функции-замыкания get_extremum
    get_min_or_max = utils.get_extremum(type="min")

    # пример вызова внутренней функции с передачей списка
    result = get_min_or_max([5, 3, 8, 1, 10])
    print(result) # 1

    # получаем функцию get_min_or_max из функции-замыкания get_extremum
    get_min_or_max = utils.get_extremum()

    # пример вызова внутренней функции с передачей кортежа
    result = get_min_or_max((5, 3, 8, 1, 10))
    print(result) # 10
