from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.forms import AskForm, AnswerForm


from qa.models import Question, Answer


def test (request,*args,**kwargs): 
    return HttpResponse('OK')

@require_GET
def index (request): 
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
        
    questions = Question.objects.new()
    limit = 10
    paginator = Paginator(questions,limit)
    page = paginator.page(page)
    
    return render(request, 'index.html', {
        'paginator': paginator,
        'questions': page.object_list,
        'page': page, })

@require_GET
def popular (request): 
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
        
    questions = Question.objects.popular()
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
    #try:
    #    answers = Answer.objects.filter(question=question)
    #except Answer.DoesNotExist:
    #        answers = None 
    return render(request, 'question_details.html', {
        'question' : question,
     #   'answers' : answers.all()[:],
    })

def ask_add (request): 
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask_add_form.html', {
        'form' : form,
    })
