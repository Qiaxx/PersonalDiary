from django.contrib import admin

from diary.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at",)
    list_filter = ("title", "created_at",)
    search_fields = ("id", "title", "content",)