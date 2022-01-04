from time import ctime

def number_of_vowels(s):
    vowels = 'aiueo'
    c = 0
    for i in s.lower():
        if i in vowels:
            c = c + 1
    return c

def number_of_consonants(x):
    consonants = 'qwrtypsdfghjklzxcvbnm'
    p = 0
    for i in x.lower():
        if i in consonants:
            p = p + 1
    return p

day = { 'Sun' : 'Ahad',
        'Mon' : 'Senin',
        'Tue' : 'Selasa',
        'Wed' : 'Rabu',
        'Thu' : 'Kamis',
        'Fri' : 'Jumat',
        'Sat' : 'Sabtu'}

month = {'Jan' : 'Januari',
         'Feb' : 'Februari',
         'Mar' : 'Maret',
         'Apr' : 'April',
         'May' : 'Mei',
         'Jun' : 'Juni',
         'Jul' : 'Juli',
         'Aug' : 'Agustus',
         'Sep' : 'September',
         'Oct' : 'Oktober',
         'Nov' : 'November',
         'Dec' : 'Desember'}

def ubahwaktu():
    now = ctime()
    _day    = now[0:3]
    _month  = now[4:7]
    _date   = now[8:10]
    _clock  = now[11:19]
    _year   = now[20:24]
    sekarang = day[_day]+' '+ _date +' '+ month[_month]+' '+ _year+' '+ "Pukul "+' '+ _clock
    return sekarang

def thousandsMarker(x):
    a = (f"{x:,}" .replace(',', '.'))
    str(a)
    return a

brackets = {       0:0,
             1000000:5,
             3000000:10,
             6000000:15,
            10000000:20,
            20000000:25,
            35000000:30,
            55000000:35,
            80000000:40,}

def calculateTax(param):
    lastI = 0
    lastPercent = 0
    totalPajak = 0
    uang = param
    for x,i in brackets.items():
        loc = x - lastI
        lastI = x
        if loc > 0 and uang != 0 :
            if uang > loc:
                bebanPajak = loc * lastPercent / 100
                totalPajak += bebanPajak
                uang = uang - loc
            else:
                bebanPajak = uang * lastPercent / 100
                totalPajak += bebanPajak
                uang = 0
        lastPercent = i
    return int(totalPajak)