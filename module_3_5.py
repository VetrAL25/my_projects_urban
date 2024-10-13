def sget_multiplied_digits (number):
    str_number = str (number)

    if len(str_number)>1:

        first = int(str_number[0])

        return first * sget_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)

res = sget_multiplied_digits(5049)
print (res)
