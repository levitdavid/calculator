def lex(s):
    a = s.split()
    d = {'один': ('N', 1), 'два': ('N', 2), 'три': ('N', 3), 'четыре': ('N', 4), 'пять': ('N', 5), 'шесть': ('N', 6),
         'семь': ('N', 7), 'восемь': ('N', 8), 'девять': ('N', 9), 'десять': ('N', 10), 'одиннадцать': ('N', 11),
         'двенадцать': ('N', 12), 'тринадцать': ('N', 13), 'четырнадцать': ('N', 14), 'пятнадцать': ('N', 15),
         'шестнадцать': ('N', 16), 'семнадцать': ('N', 17), 'восемнадцать': ('N', 18), 'левятнадцать': ('N', 19),
         'двадцать': ('N', 20), 'тридцать': ('N', 30), 'сорок': ('N', 40), 'пятьдесят': ('N', 50),
         'шестьдесят': ('N', 60), 'семьдесят': ('N', 70), 'восемьдесят': ('N', 80), 'девяносто': ('N', 90),
         'плюс': ('O', '+'), 'минус': ('O', '-'), 'умножить': ('O', '*'), 'скобка': ('Е', ''),
         'открывается': ('O', '('), 'закрывается': ('O', ')'), 'на': ('E', '')}
    r = []
    for x in a:
        if x in d:
            r.append(d[x])
        else:
            r.append('Unknown')
    return r


def synt(a):
    r = []
    numb = False
    n = 0
    for x in a:
        if x[0] == 'N':
            numb = True
            n += x[1]
        else:
            if numb:
                r.append(n)
                n = 0
            numb = False
            if x[0] == 'O':
                r.append(x[1])
    if numb:
        r.append(n)
    return r


def nums(n):
    res = ''
    names = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
             'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
             'восемнадцать', 'девятнадцать']
    names2 = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
              'девяносто']
    if abs(n) >= 100:
        return 'Переполнение'
    if n < 0:
        res = 'минус '
        n = -n
    if n < 20:
        res += names[n]
        return res
    des = n // 10
    ed = n % 10
    res += names2[des]
    if ed != 0:
        res += ' ' + names[ed]
    return res.strip()


def calc(s):
    a = lex(s)
    if 'Unknown' in a:
        return 'Неизвестное слово'
    b = synt(a)
    s = ''
    for x in b: s += str(x)
    try:
        r = eval(s)
    except:
        return 'Ошибка в выражении'
    return nums(r)


s = 'семь минус шесть плюс скобка десять умножить на два скобка'
print(calc(s))
