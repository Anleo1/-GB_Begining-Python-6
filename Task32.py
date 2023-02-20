from random import randint

arr = [randint(-100, 101) for _ in range(25)]
res = []
print(arr)
minimum = int(input("Задайте минимум: "))
maximum = int(input("Задайте максимум: "))
for i, v in enumerate(arr):
    if v >= minimum and v <= maximum:
        res.append(i)
print("Массив индексов элементов в этом диапазоне: ", res)