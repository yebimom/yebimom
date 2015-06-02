from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import UserProfile
from users.models.contact import Question, Answer
from users.models.favorite import Favorite
from users.models.management import Management


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    inline_classes = ('grp-collapse grp-open',)


class UserAdmin(UserAdmin):
    list_display = [
        'username',
    ]

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline, ]
        return super(UserAdmin, self).change_view(*args, **kwargs)


class AnswerInline(admin.StackedInline):
    model = Answer
    readonly_fields = ('answer_date',)
    fields = ('answer_date', 'content')


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('is_complete', 'question_date',)
    fields = ('is_complete', 'question_date', 'user',
              'phone', 'email', 'title', 'content',)

    inlines = [AnswerInline]


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    model = Management
    readonly_fields = ('created_at', )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Favorite)
