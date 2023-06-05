#26
'''
def power(a, b):
    if b == 0:
        return 1
    return power(a, b - 1) * a

a = int(input("введите число a - "))
b = int(input("введите число b - "))
print(power(a, b))'''


#28
'''
def binary(n):
    if n == 0 or n == 1:
        return f'{n}'
    return binary(n // 2) + f'{n % 2}'

n = int(input())
print(binary(n))
'''

#28 аналитик

def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b - 1)

a = int(input("введите число a - "))
b = int(input("введите число b - "))
print(sum(a, b))
