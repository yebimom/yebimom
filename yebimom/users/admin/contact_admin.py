from django.contrib import admin
from users.models.contact import Question, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    readonly_fields = ('answer_date',)
    fields = ('answer_date', 'content')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('is_complete', 'question_date',)
    fields = ('is_complete', 'question_date', 'user',
              'phone', 'email', 'title', 'content',)

    inlines = [AnswerInline]
