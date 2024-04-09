"""
https://coderun.yandex.ru/problem/exactly-one-occur/
Задан массив a размера n. Необходимо посчитать количество уникальных элементов в данном массиве.
Элемент называется уникальным, если встречается в массиве ровно один раз.
Формат ввода
В первой строке входных данных подается одно целое число n (1≤n≤10**5).
Во второй строке входных данных подается n целых чисел, разделенных пробелами --- d1 a1 a3, 1≤a≤10**9)
Формат вывода
В единственной строке выведите ответ на задачу.
"""


def main():

    n = int(input())
    a = list(map(int, input().split()))
    a_counts = {}

    for num in a:
        if num in a_counts:
            a_counts[num] += 1
        else:
            a_counts[num] = 1

    unique_count = 0
    for count in a_counts.values():
        if count == 1:
            unique_count += 1

    print(unique_count)


if __name__ == '__main__':
    main()
