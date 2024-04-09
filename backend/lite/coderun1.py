"""
https://coderun.yandex.ru/problem/median-out-of-three
Средний элемент.
Рассмотрим три числа a, b и c. Упорядочим их по возрастанию.
Какое число будет стоять между двумя другими?
"""


def main():
    print(sorted(map(int, input().split()))[1])


if __name__ == '__main__':
    main()
