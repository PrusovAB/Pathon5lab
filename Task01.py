


rom = int(input("Введите количество строк матрицы: "))
columns = int(input("Введите количество столбцов матрицы: "))

def fill(n, m):
    a = []
    c = "."
    c1 = "*"
    
    for row in range(n):
        a.append([])
        
        for elem in range(m):
            if row % 2 == 0:
                if(elem % 2 == 0):
                    a[row].append(c)
                else:
                    a[row].append(c1)
            else:
                if(elem % 2 == 0):
                    a[row].append(c1)
                else:
                    a[row].append(c)
            print(a[row][elem],end = " ")
        print()
        

    
fill(rom,columns)