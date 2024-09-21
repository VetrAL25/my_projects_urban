# Кортеж
immutable_var=11, 345, 'box', False, 3.5
print(immutable_var)
print(type (immutable_var))
# immutable_var [1]=543
# Не удалось изменить элемент кортежа, поскольку Кортеж - неизменяемый объект.
#
#Список
mutable_list = [99, 345, 'box', True, 0.01, '3.14']
print(mutable_list)
mutable_list [1]=543
mutable_list [-1]='Число Пи'
print(mutable_list)
# В Списке элементы можно изменять.