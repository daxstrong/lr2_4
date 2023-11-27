#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = []
    for i in range(10):
        elem = int(input(f"Введите элемент {i + 1}: "))
        A.append(elem)

    # Инициализация суммы, количества итераций
    sum_result = 0
    count_result = 0

    # Цикл для обхода элементов массива
    for element in A:
        if 2 < element < 20 and element % 8 == 0:
            sum_result += element
            count_result += 1

    # Вывод результатов
    print(f"Сумма элементов: {sum_result}")
    print(f"Количество элементов: {count_result}")
