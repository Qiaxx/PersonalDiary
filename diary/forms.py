from django import forms

from diary.models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Введите текст записи', 'class': 'form-control'}),
        }
