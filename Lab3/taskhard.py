import random as rnd
import copy as cp
size = int(input("Введіть розмір КВАДРАТНОЇ матриці(за завданням 8) "))
print("Введіть 1 для самостійного заповнення матриці "
      "\nВведіть 2 для заповнення матриці випадковими числами від 1 до 100 ")
or12 = input(">>")
matrix = []
column = []
sum_all = 0
temp = 0
if or12 == '1':
    print(f'Будь ласка введіть {size} цифр через пробіл',
          "\n\x1B[3mУвага! Не вводіть більше або меньше цифр чи посторонніх символів!\x1B[0m")
    for i in range(size):
        column = input(f"Введіть цифри {i + 1} рядка: ").split()
        column_int: list[int] = [int(x) for x in column]
        matrix.append(column_int)
elif or12 == '2':
    for i in range(size ** 2):
        column.append(rnd.randint(1, 100))
    for i in range(0, size ** 2, size):
        matrix.append(column[i:i + size])
matrix2 = cp.deepcopy(matrix)
matrix3 = cp.deepcopy(matrix)
print("Матриця:")
for i in range(0, size):
    print(matrix[i])
# ////////////////
for i in range(size):  # Перше завдання
    sum_all += sum(matrix2[i])
avg = round(sum_all / size ** 2, 2)
print(f"Середнє арифметичне з {size**2} елементів матриці: {avg}")
for i in range(size):
    matrix2[i][size - i - 1] = avg
print(f"Матриця з допоміжною діагоналю, яка скадається з середнього арифметичного {avg}")
for i in range(0, size):
    print(matrix2[i])
for i in range(size):
    for j in range(0, size - 1, 2):
        matrix3[i][j] = matrix[i][j + 1]
        matrix3[i][j + 1] = matrix[i][j]
print("Матриця зі зміненними стовпцями(перший з другим, третій з четвертим тощо)")
for i in range(0, size):
    print(matrix3[i])