def main():
    """
    https://coderun.yandex.ru/problem/gcd-and-lcm-yandex
    Решение задачи о нахождении количества пар (p, q), которые могут сгенерировать открытый ключ (x, y)
    """

    def greatest_common_divisor(p, q):
        """Поиск наибольшего общего делителя"""
        while q:
            p, q = q, p % q  # Евклидов алгоритм для нахождения НОД
        return p  # Возвращаем НОД для p и q

    def find_divisors(n):
        """Поиск всех делителей"""
        all_divisors = set()
        # Итерация до корня из n, т.к. делители идут парами, давно в интернете такое решение нашёл
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                all_divisors.add(i)
                all_divisors.add(n // i)
        return all_divisors

    def solve(x, y):
        if y % x != 0:
            return 0  # Если y не кратно x, то НОК и НОД не подходят

        z = y // x  # Вычисляем z как y деленное на x, это должно быть произведение (p/x)*(q/x)
        divisors = find_divisors(z)  # Находим все делители z
        count = 0  # Счетчик пар (p, q), удовлетворяющих условиям

        for d in divisors:
            d_pair = z // d  # Для каждого делителя d находим парный делитель
            if greatest_common_divisor(d, d_pair) == 1:  # Проверяем простоту d и d_pair
                if greatest_common_divisor(d, d_pair) == 1:
                    # Учитываем пары (p, q) и (q, p) как одну уникальную пару
                    count += 1

        return count  # Возвращаем итоговое количество подходящих пар (p, q)

    a, b = map(int, input().split(' '))
    print(solve(a, b))


if __name__ == '__main__':
    main()

