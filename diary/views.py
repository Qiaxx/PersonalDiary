from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from rest_framework.permissions import IsAuthenticated

from diary.forms import RecordForm
from diary.models import Record
from users.permissions import IsOwner


def index(request):
    return render(request, "diary/index.html")


class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    template_name = "diary/diary.html"
    context_object_name = "diary_entries"

    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q', '')
        queryset = Record.objects.filter(user=user)  # Фильтрация по владельцу

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = "diary/record_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecordDetailsView(DetailView):
    model = Record
    template_name = 'diary/detail_record.html'
    permission_classes = [IsAuthenticated, IsOwner]



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

