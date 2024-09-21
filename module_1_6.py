# Словари
print()
print('Словари.')
my_dict={'Александр' : 2013,'Илья' : 2009,'Людмила' : 1980,'Отец' : 1965 }
print(my_dict)
print(my_dict.get('Илья'))
print(my_dict.get('Иван'))
my_dict.update({'Дедушка' : 1948,
                'Бабушка' : 1953})
x=my_dict.pop('Отец')
print(x)
print(my_dict)
#Множества
my_set={21, 22, 23, 'Нога', 'Хвост', 23, 'Хвост', 21}
print()
print('Множества!')
print(my_set)
my_set.add(False)
my_set.add('Голова')
my_set.remove(22)
print(my_set)
my_set.update({8,9,8,9,10})
print(my_set)