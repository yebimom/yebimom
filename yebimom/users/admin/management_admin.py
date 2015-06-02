from django.contrib import admin
from users.models.management import Management


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    model = Management
    readonly_fields = ('created_at', )
