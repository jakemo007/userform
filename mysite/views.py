#I created this file
from django.http import HttpResponse
from django.shortcuts import render
import datetime
def index(request):
    return render(request,'index.html')
def userform(request):
    username = request.GET.get('username', '')
    DOB = request.GET.get('DOB', '')
    mail = request.GET.get('mail', '')
    cellno = request.GET.get('cellno', '')
    information = {}
    if len(username) == 0 :
        information ['name'] = 'Please enter Name '
    else : information ['name'] = 'Name is Valid '
    yr = 2020 - int(DOB.split('-')[0])
    if yr <=18:
        information['DOB'] = 'You must be 18 '
    else : information ['DOB'] = 'Above 18 '
    z = mail.split('@')
    if '@' in mail and '.' in z[1]:git init
        information['mail'] = 'Email is valid '
    else : information['mail'] = 'Email is  not  valid '
    try:
        ph = int(cellno)
        if len(cellno) != 10 and ph > 1:information['cellno'] = 'musty be 10 digit and numerical '
        else : information['cellno'] =  "is valid"
    except :
        information['cellno'] = 'musty be 10 digit and numerical '
    return render(request, 'userform.html', information)