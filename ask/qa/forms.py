from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    
 #   def __init__(self,**kwargs):
 #       super(AskForm,self).__init__(**kwargs)
        
    def clean(self): pass
    
    def save(self):
        question = Question.objects.create(**self.cleaned_data)
        #question.author_id = self._user.id
        question.save()
        return question
        

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()
    
 #   def __init__(self,**kwargs):
 #       super(AnswerForm,self).__init__(**kwargs)
        
    def clean(self): pass
    
    def save(self):
        answer = Answer.objects.create(**self.cleaned_data)
        #answer.author_id = self._user.id
        answer.save()
        return answer
    
