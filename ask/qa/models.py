from __future__ import unicode_literals
from django.db import models

#Question - вопрос
#title - заголовок вопроса
#text - полный текст вопроса
#added_at - дата добавления вопроса
#rating - рейтинг вопроса (число)
#author - автор вопроса
#likes - список пользователей, поставивших "лайк"
class Question(models.model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField()
  rating = models.IntegerField()
  author = models.CharField(max_length=255)
  likes = models.TextField()
#Answer - ответ
#text - текст ответа
#added_at - дата добавления ответа
#question - вопрос, к которому относится ответ
#author - автор ответа
class Answer(models.model):
  text = models.TextField()
  added_at = models.DateTimeField()
  question = models.TextField()
  author = models.CharField(max_length=255)
  
  class User(models.User): pass
  
#QuestionManager - менеджер модели Question
#new - метод возвращающий последние добавленные вопросы
#popular - метод возвращающий вопросы отсортированные по рейтингу
class QuestionManager(models.Manager):                                          
        def new(self):                                                              
                return self.order_by('-added_at')                                                          
        def popular(self):                                                          
                return self.order_by('-rating')

class Question(models.Model):                                                   
        objects = QuestionManager() 

