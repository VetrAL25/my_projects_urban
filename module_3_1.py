calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains (string, list_to_search):
    count_calls()
    string = string.lower()
    return string in [x.lower() for x in list_to_search]
print(string_info('Maxim'))
print(string_info('Hello exelent world'))
print(string_info('AbraCadabrA'))
print(is_contains('Hello', ['Hello world', 'Privet', 'hELLO']))
print(is_contains('pop', ['popArt', 'POP', 'VOIN']))
print(is_contains('pop', ['p o p A r t', 'bob', 'VOIN']))
print(calls)