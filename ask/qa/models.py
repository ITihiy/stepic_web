from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True, blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User)
    objects = QuestionManager()

    def get_absolute_url(self):
        return reverse('question', args=[self.id])


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
