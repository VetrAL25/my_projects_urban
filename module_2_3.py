my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
nomer = 0
while len (my_list)>nomer:
    if my_list [nomer] > 0:
        print(my_list [nomer])
        nomer += 1
        if my_list [nomer] > 0:
            continue
        if my_list[nomer] == 0:
         nomer += 1
        continue
    if my_list[nomer] < 0:
        break
