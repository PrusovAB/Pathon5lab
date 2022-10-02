# Посчитать в файле 1.txt (там может быть все что угодно)
# количество слов длины 5


file = open("text.txt","rt", encoding="utf-8")
text = file.read()

array = text.split()

sumMaxCount = 5
sumMoreFive = 0 

for elem in array:
    
    if len(elem) >= sumMaxCount:
        sumMoreFive += 1
    

print(f"Количество слов длина которых больше пяти =  {sumMoreFive}")
file.close()

