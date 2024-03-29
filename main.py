def prim(graph):
    used_versh = [0]  # список используемых вершин
    using_rebr = []  # список ребер итогового дерева
    while len(used_versh) < len(graph):  # пока все вершины графа не будут использованы
        min_weight = 10**10
        rebro = None
        for versh in used_versh:  # для каждой вершины включенной в остовное дерево
            for i in range(len(graph[versh])):  # смотри пути в остальные вершины
                # и если вес ребра не равен 0(т.е. отсутствует), найденное ребро - это не ребро между уже используемыми
                # вершинами, найденное ребро - минимальное на данном проходе по сравнению с прошлыми, то
                if graph[versh][i] != 0 and i not in used_versh and graph[versh][i] < min_weight:
                    min_weight = graph[versh][i]  # в минимальный вес записываем вес ребра
                    rebro = (versh + 1, i + 1)  # запоминаем это ребро
        # добавляем найденное ребро в остовное дерево
        used_versh.append(rebro[1] - 1)
        using_rebr.append(rebro)
    return using_rebr


matrix1 = [
    [0, 10, 11, 12, 4, 7, 10, 16, 12, 16, 4, 5, 7, 13, 9],
    [10, 0, 12, 8, 10, 3, 6, 8, 13, 6, 14, 13, 10, 16, 13],
    [11, 12, 0, 6, 4, 17, 10, 14, 10, 5, 5, 7, 9, 9, 9],
    [12, 8, 6, 0, 12, 7, 4, 17, 16, 5, 4, 13, 11, 3, 5],
    [4, 10, 4, 12, 0, 16, 13, 4, 8, 16, 11, 17, 6, 12, 13],
    [7, 3, 17, 7, 16, 0, 4, 7, 13, 14, 6, 10, 3, 11, 6],
    [10, 6, 10, 4, 13, 4, 0, 7, 14, 6, 4, 15, 7, 3, 15],
    [16, 8, 14, 17, 4, 7, 7, 0, 5, 17, 15, 16, 16, 5, 12],
    [12, 13, 10, 16, 8, 13, 14, 5, 0, 6, 7, 17, 4, 13, 13],
    [16, 6, 5, 5, 16, 14, 6, 17, 6, 0, 4, 4, 14, 7, 12],
    [4, 14, 5, 4, 11, 6, 4, 15, 7, 4, 0, 4, 5, 10, 6],
    [5, 13, 7, 13, 17, 10, 15, 16, 17, 4, 4, 0, 12, 10, 12],
    [7, 10, 9, 11, 6, 3, 7, 16, 4, 14, 5, 12, 0, 5, 11],
    [13, 16, 9, 3, 12, 11, 3, 5, 13, 7, 10, 10, 5, 0, 11],
    [9, 13, 9, 5, 13, 6, 15, 12, 13, 12, 6, 12, 11, 11, 0]
]
matrix2 = [
    [0, 17, 12, 8, 8, 14, 13, 11, 10, 10, 15, 11, 5, 13, 15],
    [17, 0, 6, 8, 16, 10, 6, 13, 15, 13, 16, 13, 14, 16, 4],
    [12, 6, 0, 9, 15, 15, 8, 12, 14, 17, 11, 5, 14, 7, 3],
    [8, 8, 9, 0, 15, 9, 3, 5, 7, 13, 8, 17, 17, 3, 7],
    [8, 16, 15, 15, 0, 16, 8, 3, 14, 6, 5, 5, 7, 4, 14],
    [14, 10, 15, 9, 16, 0, 15, 9, 8, 12, 4, 5, 13, 10, 10],
    [13, 6, 8, 3, 8, 15, 0, 15, 6, 17, 8, 8, 9, 10, 7],
    [11, 13, 12, 5, 3, 9, 15, 0, 8, 7, 6, 13, 13, 8, 9],
    [10, 15, 14, 7, 14, 8, 6, 8, 0, 3, 12, 14, 5, 4, 17],
    [10, 13, 17, 13, 6, 12, 17, 7, 3, 0, 8, 11, 16, 16, 9],
    [15, 16, 11, 8, 5, 4, 8, 6, 12, 8, 0, 8, 6, 14, 4],
    [11, 13, 5, 17, 5, 5, 8, 13, 14, 11, 8, 0, 14, 13, 14],
    [5, 14, 14, 17, 7, 13, 9, 13, 5, 16, 6, 14, 0, 8, 11],
    [13, 16, 7, 3, 4, 10, 10, 8, 4, 16, 14, 13, 8, 0, 5],
    [15, 4, 3, 7, 14, 10, 7, 9, 17, 9, 4, 14, 11, 5, 0]
]
matrix3 = [
    [0, 5, 15, 11, 15, 4, 17, 3, 13, 16, 16, 14, 4, 8, 3],
    [5, 0, 8, 10, 4, 5, 13, 7, 7, 6, 6, 10, 11, 16, 12],
    [15, 8, 0, 16, 6, 7, 14, 10, 11, 14, 5, 11, 5, 7, 16],
    [11, 10, 16, 0, 13, 4, 16, 4, 12, 3, 8, 14, 5, 15, 16],
    [15, 4, 6, 13, 0, 14, 16, 5, 8, 7, 10, 16, 17, 10, 10],
    [4, 5, 7, 4, 14, 0, 17, 15, 3, 17, 8, 15, 17, 8, 14],
    [17, 13, 14, 16, 16, 17, 0, 13, 11, 8, 16, 6, 7, 12, 16],
    [3, 7, 10, 4, 5, 15, 13, 0, 16, 11, 8, 8, 15, 13, 9],
    [13, 7, 11, 12, 8, 3, 11, 16, 0, 5, 7, 16, 16, 17, 12],
    [16, 6, 14, 3, 7, 17, 8, 11, 5, 0, 5, 11, 6, 7, 14],
    [16, 6, 5, 8, 10, 8, 16, 8, 7, 5, 0, 7, 15, 3, 4],
    [14, 10, 11, 14, 16, 15, 6, 8, 16, 11, 7, 0, 7, 11, 9],
    [4, 11, 5, 5, 17, 17, 7, 15, 16, 6, 15, 7, 0, 6, 17],
    [8, 16, 7, 15, 10, 8, 12, 13, 17, 7, 3, 11, 6, 0, 17],
    [3, 12, 16, 16, 10, 14, 16, 9, 12, 14, 4, 9, 17, 17, 0]
]

result1 = prim(matrix1)
print('Результат с 1ой матрицей:', result1)
result2 = prim(matrix2)
print('Результат со 2ой матрицей:', result2)
result3 = prim(matrix3)
print('Результат с 3ей матрицей:', result3)

# ЭТОТ КОД СНИЗУ ПОМОГАЛ СГЕНЕРИРОВАТЬ МАТРИЦЫ

# from random import randint
#
# A = []
# for i in range(15):
#     a = [0] * 15
#     A.append(a)
# for i in range(15):
#     for j in range(15):
#         if i != j:
#             if A[i][j] == 0:
#                 A[i][j] = randint(3, 17)
#                 A[j][i] = A[i][j]
# for i in A:
#     print(f'{i},')
