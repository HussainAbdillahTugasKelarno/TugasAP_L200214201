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
