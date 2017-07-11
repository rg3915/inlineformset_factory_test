from django import forms
from .models import TaskAnswer, TaskAnswerFile

class TaskAnswerForm(forms.ModelForm):

    class Meta:
        model = TaskAnswer
        fields = '__all__'


class TaskAnswerFileForm(forms.ModelForm):

    class Meta:
        model = TaskAnswerFile
        fields = '__all__'
