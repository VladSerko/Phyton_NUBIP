from random import randint

first_array = []
second_array = []
max_number = 0
for i in range(30):
    first_array.append(randint(-100, 100))
print("\n")
print("Список 30 случайных чисел:",first_array)
for i in first_array:
    if i > max_number:
        max_number = i
print("Максимальное число из списка:",max_number,"с индексом:",first_array.index(max_number))
print("\n")
for i in first_array:
    if i % 2 == 0:
        continue
    else: second_array.append(i)
second_array.sort(reverse = True)
print("Список отсортированных по убыванию элементов из списка #1:",second_array)