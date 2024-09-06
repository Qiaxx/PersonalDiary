from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from diary.forms import RecordForm
from diary.models import Record


def index(request):
    return render(request, "diary/index.html")


class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    template_name = "diary/diary.html"
    context_object_name = "diary_entries"

    def get_queryset(self):
        return Record.objects.filter(user=self.request.user)


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = "diary/diary.html"


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'diary/edit_record.html'
    success_url = reverse_lazy('diary:diary')


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('diary:diary')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

