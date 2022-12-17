# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ
# ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование
#  библиотеки Random для и получения случайного int

from random import randint as RI

my_list = []

n = 1

for i in range(n):
    my_list.append(RI(10,99))
print(my_list)

def Mixed_list_one(list, n):
    mixed_list = []
    while(n !=0 ):
        n-=1
        i = RI(0,n)
        mixed_list.append(list[i])
        list.pop(i)
    return mixed_list
# первый метод который пришел в голову, но мне кажеться более затратным
def Mixed_list_two(list):
    for i in range(0,len(list)-1):
        index_mix = RI(0,n-1)
        help = list[i]
        list[i] = list[index_mix]
        list[index_mix] = help

help_list = my_list
Mixed_list_two(my_list)
print(my_list)

help_list = Mixed_list_one(help_list, n)
print(help_list)


