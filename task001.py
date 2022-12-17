# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = float(input('Enter float number '))
n = str(n)
n = n.replace('.','')
n = n.replace('0','')
n = int(n)
sum = 0
while(n!=0):
    sum = sum + n % 10
    n //= 10

print(sum)