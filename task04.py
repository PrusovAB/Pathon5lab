# Пусть есть шахматная доска 8х8 и номера клеток a и b, где стоит
# ладья. Покажите симоволом *, где стоит ладья и символами ! - все
# возможные пути, куда она может пойти


# Размер шахматной доски.
a = 8
b = 8




#   Нарисуем шахматную доску из нулей
def newMatrix(m,n):
    matrix = []
    for row in range(m):
        matrix.append([])
        for elem in range(n):
            matrix[row].append(0)
    return(matrix)

newBoard = newMatrix(a,b)



#  Напечатыем доску

def printMatrix(matrix):

    for i in range(len(matrix)):
        
        for j in range(len(matrix[i])):
            print(matrix[i][j],end ="  ")
        print()



import random

#  Расположение рандомное ладьи на доске 8х8

sizeMatrixLine = random.randint(0,7)
sizeMatrixСolumn = random.randint(0,7)


#  Покажем все возможные ходы ладьй символом ! 

def findRook(matrix,a,b):
    
    for i in range(len(matrix)):
            if i == a:
                for j in range(len(matrix)):
                    matrix[i][j] = "!"
    for row in range(len(matrix)):
        matrix[row][b] = "!"
    matrix[a][b] = "*"

    return matrix              
    
    
newAr = findRook(newBoard,sizeMatrixLine,sizeMatrixСolumn)


printMatrix(newAr)