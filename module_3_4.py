def single_root_words (root_word, *other_word):
    same_word = []
    for i in other_word:
        if i.lower() in root_word.lower() or root_word.upper() in i.upper():
            same_word.append(i)
    return same_word
res1 = single_root_words('ПИК', 'Пикап', 'кипа', 'ПиЛкА', 'тУПИк' ,'тРОПики')
res2 = single_root_words('наборщик', 'боРЩ', 'роба', 'БОР', 'забор' ,'набор')
print (res1)
print (res2)