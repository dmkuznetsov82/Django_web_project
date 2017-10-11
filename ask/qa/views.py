from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.forms import AskForm, AnswerForm, SignupForm
from django.contrib.auth import authenticate, login


from qa.models import Question, Answer


def test (request,*args,**kwargs): 
    return HttpResponse('OK')

def signup (request,id): 
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.raw_password
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup_form.html', {
        'form': form,
        'user': request.user,
        'session': request.session, })

def login (request,id): 
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username, password)
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'user': request.user,
        'session': request.session, })

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

def question_details (request,id): 
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'question_details.html', {
        'question' : question,
        'form' : form,
    })

def ask_add (request): 
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask_add_form.html', {
        'form' : form,
    })
