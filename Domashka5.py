#26
'''
def step(a,b):
    if b == 0:
        return 1
    return pow(a,b)
a = int(input("Введите A: "))
b = int(input("Введите B: "))
print(step(a,b))
'''
#28

def sist(a):
    txt = " "
    while a > 0:
        txt = str(a % 2) + txt
        a //=2
    return txt
a = int(input("Введите чило: "))
   
print(sist(a))

