from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random

def ex(request):
    return render(request, 'generator/index.html')
def password(request):
    char1 = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char1.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialchar'):
        char1.extend(list('!@#$%&^*'))
    if request.GET.get('digits'):
        char1.extend(list('1234567890'))

    thepass = ' '
    length = int(request.GET.get('length'))
    for i in range(length):
        thepass += random.choice(char1)

    return render(request, 'generator/password.html',{'password': thepass})
