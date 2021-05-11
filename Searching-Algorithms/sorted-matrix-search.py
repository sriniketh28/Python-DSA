def sorted_matrix_search(matrix, x):
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if x == matrix[i][j]:
            return [i,j]
        if x > matrix[i][j]:
            i += 1
        else:
            j -= 1
    return str(x)+" is not in matrix"

matrix = [[3, 30, 38],
          [36, 43, 60],
          [40, 51, 69]]

print(sorted_matrix_search(matrix, 69))
print(sorted_matrix_search(matrix, 62))

