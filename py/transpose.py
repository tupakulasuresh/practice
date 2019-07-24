def transpose(matrix):
    matrix_len = len(matrix)
    return [[matrix[j][i] for j in range(matrix_len)] for i in (range(len(matrix[0])))]
