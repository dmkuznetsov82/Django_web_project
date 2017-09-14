from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 

class QuestionManager(models.Manager):                                          
        def new(self):                                                              
                return self.order_by('-added_at')                                                          
        def popular(self):                                                          
                return self.order_by('-rating')
          
class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField()
  rating = models.IntegerField()
  author = models.ForeignKey(User,related_name='question_author',default='test')
  likes = models.ManyToManyField(User)
  objects = QuestionManager() 

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField()
  question = models.TextField()
  author = models.ForeignKey(User)
   
