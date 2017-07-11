from django import forms
from .models import TaskAnswer, TaskAnswerFile


class TaskAnswerForm(forms.ModelForm):

    class Meta:
        model = TaskAnswer
        fields = ('candidate',)


class TaskAnswerFileForm(forms.ModelForm):

    class Meta:
        model = TaskAnswerFile
        fields = ('answer_file',)
