from django import forms
import models

class CreatePoll(forms.Form):
    question_title = forms.CharField(widget = forms.TextInput(attrs = {'class':'required', 'size':50}), help_text = 'Title for your poll. This is required.')
    question_text = forms.CharField(widget = forms.Textarea, help_text = 'Some description. This is required.')
    choice_1 = forms.CharField(widget = forms.TextInput(attrs = {'class':'required', 'size':50}), help_text = 'Allowed choices for the poll. At least two are required.')
    choice_2 = forms.CharField(widget = forms.TextInput(attrs = {'class':'required', 'size':50}))
    choice_3 = forms.CharField(required = False, widget = forms.TextInput(attrs = {'size':50}))
    choice_4 = forms.CharField(required = False, widget = forms.TextInput(attrs = {'size':50}))
    choice_5 = forms.CharField(required = False, widget = forms.TextInput(attrs = {'size':50}))
    choice_6 = forms.CharField(required = False, widget = forms.TextInput(attrs = {'size':50}))
    choice_7 = forms.CharField(required = False, widget = forms.TextInput(attrs = {'size':50}))
    choice_8 = forms.CharField(required = False, widget = forms.TextInput(attrs = {'size':50}))
    
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(forms.Form, self).__init__(*args, **kwargs)
        
    def save(self):
        question = models.Question(title = self.cleaned_data['question_title'], text = self.cleaned_data['question_text'])
        question.save()
        for field in self.fields:
            if field in ['question_title','question_text']:
                continue
            if self.cleaned_data[field]:
                choice = models.Choice(question = question, text = self.cleaned_data[field])
                choice.save()
        return question