zveri=['медведи', 'волки', 'зайцы']
print(zveri[1])
zveri[1]='черепахи'
print(zveri)
zveri.append(True)
print(zveri)
zveri.append(777)
print(zveri)
zveri.extend(['Tru', 333, 'doo'])
print(zveri)
zveri.remove(True)
print('doo' in zveri)
print(zveri)
zveri.remove('doo')
print(zveri)
print('doo' not in zveri)
print(zveri[1:4:2])