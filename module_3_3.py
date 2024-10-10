def print_params (a = 1, b  = 'строка', c = True):
    print(a, b, c)
#
print('Функция с параметрами по умолчанию:')
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print('')
print('Распаковка параметров:')
values_list = [1, 3.14, 'spisok']
values_dict = {'a':8, 'b':'part', 'c':False}
print_params(*values_list)
print_params(**values_dict)
print('')
print('Распаковка + отдельные параметры:')
values_list2 = [555, 'Anapa']
print_params(*values_list2, 42)