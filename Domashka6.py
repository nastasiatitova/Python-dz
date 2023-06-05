#30
'''
a = int(input("введите первое число - "))
d = int(input("введите разницу - "))
n = int(input("введите количество элементов - "))
num = 0
list = []
for i in range(n):
    num = a + i*d
    list.append(num)

print(*list)'''

#32 

n = int(input("Введите количество элементов списка: "))
x = int(input("Введите первое число диапозна: "))
y = int(input("Введите второе число диапозна: "))

list = [int(i) for i in input("Введите элементы списка: ").split()]

for i in range(n):
    if list[i] > x and list[i] < y:
        print(i, end=' ')