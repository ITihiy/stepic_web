from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from .forms import AskForm, AnswerForm, SignupForm, LoginForm


# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    questions = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'qa/index.html', context={'questions': page.object_list})


def popular(request):
    questions = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'qa/popular.html', context={'questions': page.object_list})


def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = AnswerForm()
    return render(request, 'qa/question.html', context={'question': question, 'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = Question(title=form.cleaned_data['title'], text=form.cleaned_data['text'])
            question.author = request.user
            question.save()
            return redirect(question)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', context={'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', context={'form': form})


def login_(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')

    else:
        form = LoginForm()
    return render(request, 'qa/login.html', context={'form': form})


