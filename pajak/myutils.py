def number_of_vowels(s):
    vowels = 'aiueo'
    c = 0
    for i in s.lower():
        if i in vowels:
            c = c + 1
    return c

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