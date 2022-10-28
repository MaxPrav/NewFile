from re import A


s = 0
number = input('Введите число: ')
res=list(map(int, [ch for ch in number if ch.isdigit()]))
for el in res:
    s+=el
print(s)