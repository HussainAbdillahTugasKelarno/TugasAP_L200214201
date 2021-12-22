from django.shortcuts import render
from time import ctime
from .myutils import number_of_vowels
from .myutils import number_of_consonants
from .myutils import ubahwaktu

def coba(request):
    s = ubahwaktu()
    context = {
        'judul' : 'Tugas AP 2021',
        'nama'  : 'Hussain Abdillah Tugas Kelarno',
        'NIM'   : 'L200214201',
        'waktu' : s,
        'pesan' : 'Hello my friends, apa kabar ? I hope everything is good.',
    }

    if request.POST:
        st = request.POST.get('kalimat')
        v = number_of_vowels(st)
        c = number_of_consonants(st)
        context.update( { 'kal'        : st, 
                          'vowels'     : v,  
                          'consonants' : c  } )

    return render(request, 'pajak/index.html', context)
