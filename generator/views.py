from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')
    # return HttpResponse('Hello there friend!')


def password(request):
    thepassword = ''
    length = int(request.GET.get('length'), 12)
    pool = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        pool.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        pool.extend(list('0123456789'))

    if request.GET.get('special'):
        pool.extend(list('!@#$%^&*()'))

    for x in range(length):
        thepassword += choice(pool)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
