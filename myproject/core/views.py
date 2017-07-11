from django.shortcuts import render, resolve_url
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from .models import TaskAnswer, TaskAnswerFile
from .forms import TaskAnswerForm, TaskAnswerFileForm


def home(request):
    order_forms = TaskAnswer()
    item_order_formset = inlineformset_factory(
        TaskAnswer, TaskAnswerFile, form=TaskAnswerFileForm, extra=0, can_delete=False,
        min_num=1, validate_min=True)

    if request.method == 'POST':
        forms = TaskAnswerForm(request.POST, request.FILES,
                         instance=order_forms, prefix='main')
        formset = item_order_formset(
            request.POST, request.FILES, instance=order_forms, prefix='taskanswer')

        if forms.is_valid() and formset.is_valid():
            forms = forms.save()
            formset.save()
            return HttpResponseRedirect(resolve_url('home'))
    else:
        forms = TaskAnswerForm(instance=order_forms, prefix='main')
        formset = item_order_formset(instance=order_forms, prefix='taskanswer')

    context = {
        'forms': forms,
        'formset': formset,
    }

    return render(request, 'index.html', context)

