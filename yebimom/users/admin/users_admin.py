from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from users.models import UserProfile
from django.contrib.auth.models import User


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


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
