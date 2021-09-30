from django.contrib import admin
from .models import Quiz, Question, Answer


class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('date_started',)


class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('quiz_id',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question)
