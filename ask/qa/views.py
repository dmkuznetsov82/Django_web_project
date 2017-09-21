from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

from qa.models import Question, Answer


def test (request,*args,**kwargs): 
    return HttpResponse('OK')

def index (request,*args,**kwargs): 
    return HttpResponse('Index')

@require_GET
def popular (request): 
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
        
    questions = Question.object.popular()
    limit = 10
    paginator = Paginator(questions,limit)
    page = paginator.page(page)
    
    return render(request, 'popular.html', {
        'paginator': paginator,
        'questions': page.object_list,
        'page': page, })

@require_GET
def question_details (request,id): 
    question = get_object_or_404(Question, id=id)
    try:
        answers = Answer.object.filter(question=question)
    except Answer.DoesNotExist:
            answers = None 
    return render(request, 'question_details.html', {
        'question' : question,
        'answers' : answers.all()[:],
    })
