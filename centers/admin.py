from django.contrib import admin

# Model
from centers.models.center import Center

# Models
from centers.models import CenterImage


admin.site.register(Center)


@admin.register(CenterImage)
class CenterImageAdmin(admin.ModelAdmin):
    pass
