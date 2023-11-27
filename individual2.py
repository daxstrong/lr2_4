#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Ввод списка вещественных элементов
    float_list = []
    num_elements = int(input("Введите количество элементов списка: "))
    for i in range(num_elements):
        elem = float(input(f"Введите элемент {i + 1}: "))
        float_list.append(elem)

    # Ввод диапазона [A, B]
    A = float(input("Введите значение A: "))
    B = float(input("Введите значение B:"))

    # Количество элементов в диапазоне [A, B]
    count_in_range = 0
    for elem in float_list:
        if A <= elem <= B:
            count_in_range += 1

    # Сумма элементов после максимального элемента
    max_value = max(float_list)
    max_index = float_list.index(max_value)
    sum_after_max = 0
    if max_index < num_elements - 1:
        sum_after_max = sum(float_list[max_index + 1:])

    # Упорядочивание элементов по убыванию модулей
    float_list.sort(key=lambda x: abs(x), reverse=True)

    # Вывод результатов
    print(f"1. Количество элементов в диапазоне от {A} до {B}: {count_in_range}")
    print(f"2. Сумма элементов списка, расположенных после максимального элемента: {sum_after_max}")
    print("Упорядоченные элементы по убыванию модулей:", float_list)
