from django import forms
from qa.models import Question, Answer, User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Username is required but not set')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('User already exists')
        except User.DoesNotExist:
            pass
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required but not set')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Password is required but not set')
        self.raw_password = password
        return make_password(password)
    
    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField( max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Username is required')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Password is required')
        return password

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Incorrect username or password')
        if not user.check_password(password):
            raise forms.ValidationError('Incorrect username or password')

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    
    def clean(self): pass
    
    def save(self):
        question = Question.objects.create(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question
        

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()
        
    def clean(self): pass
    
    def save(self):
        answer = Answer.objects.create(**self.cleaned_data)
        #answer.author_id = self._user.id
        answer.save()
        return answer
    
