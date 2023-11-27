#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определение массива A с использованием List Comprehension
    A = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]

    # Вычисление суммы и количества с использованием List Comprehension
    sum_result = sum(element for element in A if 2 < element < 20 and element % 8 == 0)
    count_result = len([element for element in A if 2 < element < 20 and element % 8 == 0])

    # Вывод результатов
    print(f"Сумма элементов: {sum_result}")
    print(f"Количество элементов: {count_result}")
