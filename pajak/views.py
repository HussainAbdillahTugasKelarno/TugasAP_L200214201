from django.shortcuts import render
from django.http import HttpResponse

from time import ctime

def coba(request):
    now = ctime()
    tm = "<html><body><h1>My name is <i>{nama}</i></h1><h2>It is now {waktu}</h2><hr></body></html>"
    hasil = tm.format(nama = "Hussain", waktu = now)
    return HttpResponse(hasil)
