from django.contrib import admin

# Models
from centers.models import CenterImage


@admin.register(CenterImage)
class CenterImageAdmin(admin.ModelAdmin):
    pass
