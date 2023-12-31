# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Ввод количества элементов для первого и второго множеств
n = int(input("Введите количество элементов в первом множестве: "))
m = int(input("Введите количество элементов во втором множестве: "))

# Инициализация пустых множеств для первого и второго наборов
set1 = set()
set2 = set()

# Ввод элементов для первого множества
print("Введите элементы для первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

# Ввод элементов для второго множества
print("Введите элементы для второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

# Нахождение пересечения множеств
intersection = set1.intersection(set2)

# Преобразование пересечения в список и сортировка
result_list = sorted(list(intersection))

# Вывод результата
print("Числа, которые встречаются в обоих наборах в порядке возрастания:")
for num in result_list:
    print(num)
