from django.shortcuts import render, resolve_url
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django.views.generic import TemplateView
from .models import TaskAnswer, TaskAnswerFile
from .forms import TaskAnswerForm, TaskAnswerFileForm


def home(request):
    return render(request, 'index.html')


def taskanswer(request):
    order_form = TaskAnswer()
    item_order_formset = inlineformset_factory(
        TaskAnswer, TaskAnswerFile, form=TaskAnswerFileForm, extra=0, can_delete=False,
        min_num=1, validate_min=True)

    if request.method == 'POST':
        form = TaskAnswerForm(request.POST, request.FILES,
                              instance=order_form, prefix='main')
        formset = item_order_formset(
            request.POST, request.FILES, instance=order_form, prefix='taskanswer')

        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            print(formset)
            return HttpResponseRedirect(resolve_url('taskanswer1'))
    else:
        form = TaskAnswerForm(instance=order_form, prefix='main')
        formset = item_order_formset(instance=order_form, prefix='taskanswer')

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, 'taskanswer1.html', context)


class TaskAnswerCreate(TemplateView):
    template_name = 'index2.html'

    def get_context_data(self, **kwargs):
        context = super(TaskAnswerCreate, self).get_context_data(**kwargs)
        obj = self.object

        item_order_formset = inlineformset_factory(
            TaskAnswer, TaskAnswerFile, form=TaskAnswerFileForm, extra=0,
            can_delete=False, min_num=1, validate_min=True)
        formset = item_order_formset(
            instance=TaskAnswer(), prefix='taskanswer')
        context['formset'] = formset
        return context

    def post(self, request, *args, **kwargs):

        obj = self.get_object()

        # if 'apply_btn' in request.POST:
        if self.request.POST:
            item_order_formset = inlineformset_factory(
                TaskAnswer, TaskAnswerFile, form=TaskAnswerFileForm, extra=0,
                can_delete=False, min_num=1, validate_min=True)
            formset = item_order_formset(
                instance=TaskAnswer(), prefix='taskanswer')
            formset.save()
