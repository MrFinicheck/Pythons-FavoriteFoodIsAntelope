#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести в скобках через запятую мощность и цену.
    auto = tuple(map(str, input().split()))
    # Проверить количество элементов списка.
    if len(A) != 30:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    auto_slice = tuple(map(lambda x: x[1:-1], auto))
    auto_slice2 = tuple(map(lambda x: x.split(","), auto_slice))
    auto_slice3 = [(float(a[0]), float(a[1])) for a in auto_slice2]

    # Вывести стоимость автомобилей, удовлетворяющих условию.
    for item in auto_slice3:
        if item[0] <= 80:
            print(item[1])
