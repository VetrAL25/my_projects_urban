from random import randint
number = randint(3, 20)
#print(number)
def get_password(number_):
    password = ''
    for i in range(1, 20):
        for j in range(2, 20):
            if j <= i:
                continue
            if number_ % (i + j) == 0:
                password += str(i) + str(j)
    return password
result = get_password(number)
print('Шифр для числа', number, ':', result)