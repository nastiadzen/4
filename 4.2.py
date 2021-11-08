a=0
b=0
c=0
d=set()
for i in open('текст.txt', encoding='utf-8'):
    b+=len(i)
    l=' '.join(i.splitlines()).split()
    for x in l:
        c+=len(x)
    p='out'
    for h in i:
        if h!=' ' and p=='out':
            a+=1
            p='in'
        elif h==' ':
            p='out'
    d|=set(i.split())
print("Кількість символів з пробілами ", b)
print("Кількість символів без пробілів ", c)
print("Кількість слів", a)
print("Кількість унікальних слів (слів без повторень) ", len(d))