from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET

def test (request,*args,**kwargs): 
    return HttpResponse('OK')

def new (request,*args,**kwargs): 
    return HttpResponse('OK')

def popular (request,*args,**kwargs): 
    return HttpResponse('OK')

@reguire_GET
def question_details (request,id): 
    question = get_object_or_404(Question, id=id)
    return render(request, '/question/question_details.html','question':question)
