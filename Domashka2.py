#10
'''
n = int(input("Введите количество монеток - "))
count_0 = 0
count_1 = 0
for i in range(n):
    x = int(input("монетка - "))
if x == 0:
    count_0 += 1
else:
    count_1 += 1
if count_0 < count_1:
    print('перевернуть надо монеты с решкой')
elif count_0 == count_1:
    print(f'Количество орлов и решек одинаково, по {count_1} штук')    
else:
    print('перевернуть надо монеты с орлом')'''

#12 Петя и Катя
'''
x = int(input('Введите первое натуральное число X '))
y = int(input('Введите второе натуральное число Y '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)'''

#14 

n = int(input("Введите максимальное число - "))
k=0
while 2 ** k <= n:
    print(2 ** k)
    k += 1


