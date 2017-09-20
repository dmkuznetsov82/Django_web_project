from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from qa.models import Question, Answer

def test (request,*args,**kwargs): 
    return HttpResponse('OK')

def index (request,*args,**kwargs): 
    return HttpResponse('Index')

def popular (request,*args,**kwargs): 
    return HttpResponse('Popular')

@require_GET
def question_details (request,id): 
    question = get_object_or_404(Question, id=id)
    try:
        answer = Answer.object.get(question=question)
    except Answer.DoesNotExist:
            answer = None 
    return render(request, '/question/question_details.html', {
        'question' : question,
        'answers' : answer.all()[:],
    })
