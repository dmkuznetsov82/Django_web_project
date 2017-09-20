from django.conf.urls import url
from django.contrib import admin
from qa.views import test,new_questions,popular,question_details
urlpatterns = [
    url(r'^$', new_questions),
    url(r'^popular/',popular),
    url(r'^question/?P<id>\w+/$',question_details)
]
