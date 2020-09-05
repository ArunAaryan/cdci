def nullifyRow(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

def zeroMatrix(matrix):
    row_zero = [False]* len(matrix)
    col_zero = [False] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_zero[i] = True
                col_zero[j] = True

    for i in range(len(matrix)):
        if row_zero[i]:
            nullifyRow(matrix, i)
        
    
    for j in range(len(matrix[0])):
        if col_zero[j]:
            nullifyCol(matrix, j)

matrix = [[1,1,2,3], [1,2,0,4],[5,6,7,8],[9,2,3,4]]
zeroMatrix(matrix)
for i in range(len(matrix)):
    print(matrix[i], end ="\n")