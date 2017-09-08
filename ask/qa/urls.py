from django.conf.urls import url
from django.contrib import admin
from ask.qa import views
urlpatterns = [
    url(r'^admin/', views),
]
