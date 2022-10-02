# Создать случайную матрицу (библиотека random) размера m x n,
# обнулить все элементы выше главной диагонали, записать ее в
# файл

import random

# Создаем рандомную размерность матрица от 6 до 12
sizeMatrixLine = random.randint(6,12)
sizeMatrixСolumn = random.randint(6,12)

# Функция заполняет рандомную матрицу рандомным числом от 1 до 100
def newMatrix(m,n):
    matrix = []
    

    for row in range(m):
        
        matrix.append([])
        for elem in range(n):
            numberMatrix = random.randint(1,100)
            matrix[row].append(numberMatrix)
    return(matrix)

#  Функция печатые рандомную матрицу

def printMatrix(matrix):

    

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end =" ")
        print()
    

newAr = newMatrix(sizeMatrixLine,sizeMatrixСolumn)




#  Функция заменяет все числа выше главной диоганали нулями..

def zeroingMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                for k in range(i+1,len(matrix[i])):
                    matrix[i][k] = 0
    return matrix



printMatrix(newAr)
zeroMatrix = zeroingMatrix(newAr)

print()
print()


printMatrix(zeroMatrix)


#  Записываем нашу матрицу обнуленную в фаил.
file = open("task03.txt", "w" )

for i in range(len(zeroMatrix)):
    for j in range(len(zeroMatrix[i])):
        file.write(f"{zeroMatrix[i][j]}")
        file.write(" ")
    file.write("\n")

file.close()