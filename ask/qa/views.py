from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Question

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
    return render(request, 'qa/question.html', context={'question': question})
