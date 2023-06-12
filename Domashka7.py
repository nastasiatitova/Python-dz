#34 Vinni
'''
list = [len([i for i in element if i in "АЕЁИОУЫЭЮЯаеёиоуыэюя"]) for element in input("Введите стихотворенье: ").split()]
if all([i == list[0] for i in list]):
    print("Парам пам-пам")
else:
    print("Пам парам")'''

#36

def print_operation_table(operation, x, y):
    for i in range (1, x + 1):                 
        for j in range (1, x + 1):             
            print(operation(i, j), end='\t')
        print()

num_rows = 6
num_columns = 6

print_operation_table(lambda x, y: x * y, num_rows, num_columns)

