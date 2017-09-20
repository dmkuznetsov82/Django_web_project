from django.conf.urls import url
from django.contrib import admin
from qa.views import test, question_details
urlpatterns = [
    url(r'^(?P<id>\d+)/$', question_details, name='question_details'),
]
