from django.contrib import admin

from .models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'question', 'answer', 'image')

admin.site.register(Subject)
admin.site.register(Question, QuestionAdmin)