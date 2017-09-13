from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField()
  rating = models.IntegerField()
  author = models.CharField(max_length=255)
  likes = models.TextField()

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField()
  question = models.TextField()
  author = models.CharField(max_length=255)
  
  class CustomUser(User): pass
  
class QuestionManager(models.Manager):                                          
        def new(self):                                                              
                return self.order_by('-added_at')                                                          
        def popular(self):                                                          
                return self.order_by('-rating')

class Question(models.Model):                                                   
        objects = QuestionManager() 

