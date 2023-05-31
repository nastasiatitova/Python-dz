#22  Даны два неупорядоченных набора целых чисел
'''
n = int(input("введите количество первого множества - "))
m = int(input("введите количество второго множества - "))

list_1 = [int(i) for i in input("Введие числа первого множества: ").split()]
list_2 = [int(i) for i in input("Введие числа второго множества: ").split()]
a = set(list_1)
b = set(list_2)
s =a.union(b)
print(s)'''

#24 В фермерском хозяйстве в Карелии выращивают чернику

n = int(input("введите количество кустов - "))
arr = list()
for i in range(n):
    x = int(input(f"Введите количество ягод на кусте {i+1} - "))
    arr.append(x)
arr_sum = list()
for i in range(len(arr)-1):
    arr_sum.append(arr[i-1]+arr[i]+arr[i+1])
print(max(arr_sum))


