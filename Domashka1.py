'''zad2: Найдите сумму цифр трехзначного числа.'''
'''
n = input("введите трехзначное число - ")
print("Сумма цифрр = ", + int(n[0])+int(n[1])+int(n[2]))
'''
'''zad4.Петя, Катя и Сережа делают из бумаги журавликов'''
'''
s = int(input("введите общее количество журавликов - "))

print("Петя сделал - ", + int(1/6*s))
print("Катя сделала - ", + int(4/6*s))
print("Сережа сделал - ", + int(1/6*s))
'''
'''zad6.Счастливый билет'''
'''
n = input("введите шестизначное число - ")
if int(n[0])+int(n[1])+int(n[2]) == int(n[3])+int(n[4])+int(n[5]):
    print("Ура! Счастливый билет!")
else:
    print("Не счастливый")
'''
'''zad8.можно ли от шоколадки размером n × m долек отломить k долек'''

n = int(input("введите ширину шоколадки - "))
m = int(input("введите длину шоколадки - "))
k = int(input("введите колич-во долек - "))

if k==n or k==m or k%n==0 or k%m==0:
    print("Можно") 
else:
    print("Нельзя")