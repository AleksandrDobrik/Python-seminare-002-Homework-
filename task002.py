# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Enter n '))

my_list = []
sum = 0
for i in range(1, n + 1):
    my_list.append(round((1 + 1 / i) ** i, 2))
    sum = sum + round((1 + 1 / i) ** i, 2)


print(f'Для n={n} ->', my_list)
print(f"Сумма {sum}")
