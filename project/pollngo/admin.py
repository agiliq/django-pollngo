from django.contrib import admin

from pollngo.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)