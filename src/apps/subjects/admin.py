from django.contrib import admin
from apps.subjects.models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ...