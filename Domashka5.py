#26
'''
def power(a, b):
    if b == 0:
        return 1
    return power(a, b - 1) * a

a = int(input())
b = int(input())
print(power(a, b))'''


#28
   
def binary(n):
    if n == 0 or n == 1:
        return f'{n}'
    return binary(n // 2) + f'{n % 2}'

n = int(input())
print(binary(n))



