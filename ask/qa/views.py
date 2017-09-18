from django.shortcuts import render
from django.http import HttpResponse
def test (request,*args,**kwargs): 
    return HttpResponse('OK')
def new (request,*args,**kwargs): 
    return HttpResponse('OK')
def popular (request,*args,**kwargs): 
    return HttpResponse('OK')
def question (request,*args,**kwargs): 
    return HttpResponse('OK')
