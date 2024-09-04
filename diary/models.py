from django.db import models

from users.models import User


class Record(models.Model):
    title = models.CharField(max_length=150, verbose_name="Тема записи", help_text="Введите тему записи")
    content = models.TextField(verbose_name="Содержание записи", help_text="Введите содержание записи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="records", blank=True, null=True
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.title
    