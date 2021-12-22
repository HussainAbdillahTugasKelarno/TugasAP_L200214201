from django.shortcuts import render
from time import ctime

def coba(request):
    now = ctime()
    context = {
        'judul' : 'Tugas AP 2021',
        'nama'  : 'Hussain Abdillah Tugas Kelarno',
        'NIM'   : 'L200214201',
        'waktu' : now,
        'pesan' : 'Hello my friends, apa kabar ? I hope everything is good.',
    }

    if request.POST:
        st = request.POST.get('kalimat')
        context.update( { 'kal' : st } )

    return render(request, 'pajak/index.html', context)
