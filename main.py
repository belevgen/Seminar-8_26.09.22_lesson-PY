f = open('data_pupils.txt', encoding='utf-8')
l = f.readlines()
for line in l:
    print(line.strip().split(';'))

