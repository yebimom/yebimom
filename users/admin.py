from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import UserProfile
from users.models.contact_us import Question, Answer


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]


class AnswerInline(admin.StackedInline):
    model = Answer
    readonly_fields = ('answer_date',)
    fields = ('answer_date', 'content')


class QuestionAdmin(admin.ModelAdmin):
    classes = ('grp-collapse grp-closed',)

    readonly_fields = ('is_complete', 'question_date',)
    fields = ('is_complete', 'question_date', 'user', 'content',)

    inlines = [
        AnswerInline
    ]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
