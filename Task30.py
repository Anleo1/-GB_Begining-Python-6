first_n = int(input("Введите первый элемент арифметической прогрессии: "))
diff = int(input("Разность: "))
num = int(input("Количество элементов: "))

arr = []
count = 0
while count < num:
    arr.append(first_n + count * diff)
    count+=1

print(arr)