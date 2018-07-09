# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    if request.method=='GET':
        return render(request, 'home.html')
    else:
        text=request.POST.get('text','')
        if(len(text)<10):
            return render(request, 'home.html', {'result':"Low Quality Report."})
        else:
            return render(request, 'home.html', {'result':"High Quality Report."})
