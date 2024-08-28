# Python 的列表还可以嵌套。
# 以下实例展示了 3 * 4 的矩阵列表：
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
# 以下实例将 3 * 4 的矩阵列表转换为 4 * 3 列表：

print([[row[i] for row in matrix] for i in range(4)])

# 以上实例也可以使用以下方法来实现：
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# 另外一种实现方法：
transposed = []
print(transposed)
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
    
