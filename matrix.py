import random

# Константы диапазона значений для случайной генерации матриц
MIN = -1000
MAX = 1000

############ Функции ввода ###############

# Вспомогательная функция выхода из программы на случай неверных данных
def error_exit():
    print("Неверный ввод")
    exit(1)

# Функция ввода размера матрицы
def matrix_size_input():
    y = input("Введите высоту матрицы: ")
    try:
        y = int(y)
    except:
        error_exit()
    if y < 1:
        error_exit()
    x = input("Введите ширину матрицы: ")
    try:
        x = int(x)
    except:
        error_exit()
    if x < 1:
        error_exit()
    return x, y

# Вспомогательная функиия печати матриы
def matrix_print(matrix):
    for elem in matrix:
        print(elem)

# Фнукция ввода матрицы с клавиатуры
def matrix_manual(x, y):
    matrix = []
    for i in range(y):
        n = i + 1
        inp = input(f"Введите через пробел элементы {n} строки матрицы({x} цифр): ")
        inp = inp.split()
        if len(inp) != x:
            error_exit()
        for i in range(len(inp)):
            try:
                inp[i] = int(inp[i])
            except:
                error_exit()
        matrix.append(inp)
    return matrix

# Фнукция создания случайной матрицы
def matrix_random(x, y):
    return [[random.randint(MIN, MAX) for i in range(x)] for j in range(y)]

# Итого функция ввода матрицы
def matrix_input():
    x, y = matrix_size_input()
    inp = input("Введите 0 для генерации случайной матрицы или 1 для ручного ввода: ")
    try:
        inp = int(inp)
    except:
        error_exit()
    if inp == 0:
        matrix = matrix_random(x, y)
    elif inp == 1:
        matrix = matrix_manual(x, y)
    else:
        error_exit()
    return matrix

def num_input():
    inp = input("Введите число: ")
    try:
        inp = int(inp)
    except:
        error_exit()
    return inp

############ Матричные операции ###############

# Вспомгательная функция произведения векторов
def vec_mult(vec1, vec2):
    return sum([int(x * y) for x, y in zip(vec1, vec2)])

# Транспонирование матрицы
def matrix_t(matrix):
    return [*map(list, zip(*matrix))]

# Умножение матриц
def matrix_mult(matrix1, matrix2):
    # Определяем размер результатирующей матрицы (высота первой - будет шириной, ширина второй - будет высотой)
    l, n = len(matrix1), len(matrix2[0])
    # Создаем по этому размеру нулевую матрицу
    res = [[0 for i in range(n)] for j in range(l)]
    # Заполняем эту матрицу по правилу умножения матриц
    for i in range(l):
        for j in range(n):
            vec1 = matrix1[i]
            vec2 = matrix_t(matrix2)[j]
            res[i][j] = vec_mult(vec1, vec2)
    return res

# Сложение матриц (поэлементное)
def matrix_sum(matrix1, matrix2):
    return[[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

# Скалярное произведение матрицы на число
def matrix_scalar(matrix, num):
    return [[matrix[i][j] * num for j in range(len(matrix[0]))] for i in range(len(matrix))]

# Вспомогательная функция копирования матрицы
def matrix_copy(matrix):
    return [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

# Возведение матрицы в степень
def matrix_power(matrix, num):
    size = len(matrix)
    if num == 0:
        return [[1 for i in range(size)] for j in range(size)]
    if num == 1:
        return matrix
    res = matrix_copy(matrix)
    for _ in range(num - 1):
        res = matrix_mult(res, matrix)
    return res


def main():
    print("(1) Транспонирование матрицы")
    print("(2) Умножение матриц")
    print("(3) Умножение матрицы на число")
    print("(4) Сложение матриц")
    print("(5) Возведение в степень матрицы")
    oper = input("Введите номер операции: ")
    try:
        oper = int(oper)
    except:
        error_exit()
    if oper < 1 or oper > 5:
        error_exit()
    if oper == 1:
        matrix = matrix_input()
        print("Входная матрица:")
        matrix_print(matrix)
        matrix = matrix_t(matrix)
        print("Выходная матрица:")
        matrix_print(matrix)
    elif oper == 2:
        print("Ввод первой матрицы:")
        matrix1 = matrix_input()
        print("Входная матрица1:")
        matrix_print(matrix1)
        print("Ввод второй матрицы:")
        matrix2 = matrix_input()
        if len(matrix1[0]) != len(matrix2):
            error_exit()
        print("Входная матрица2:")
        matrix_print(matrix2)
        matrix = matrix_mult(matrix1, matrix2)
        print("Выходная матрица:")
        matrix_print(matrix)
    if oper == 3:
        matrix = matrix_input()
        print("Входная матрица:")
        matrix_print(matrix)
        num = num_input()
        matrix = matrix_scalar(matrix, num)
        print("Выходная матрица:")
        matrix_print(matrix)
    elif oper == 4:
        print("Ввод первой матрицы:")
        matrix1 = matrix_input()
        print("Входная матрица1:")
        matrix_print(matrix1)
        print("Ввод второй матрицы:")
        matrix2 = matrix_input()
        if len(matrix1[0]) != len(matrix2[0]) or len(matrix1) != len(matrix2):
            error_exit()
        print("Входная матрица2:")
        matrix_print(matrix2)
        matrix = matrix_sum(matrix1, matrix2)
        print("Выходная матрица:")
        matrix_print(matrix)
    if oper == 5:
        matrix = matrix_input()
        if len(matrix) != len(matrix[0]):
            error_exit()
        print("Входная матрица:")
        matrix_print(matrix)
        num = num_input()
        if num < 0:
            error_exit()
        matrix = matrix_power(matrix, num)
        print("Выходная матрица:")
        matrix_print(matrix)
    while True:
        input("Нажмите Enter для выхода")
        break


if __name__ == "__main__":
    main()
