from django.contrib import admin

# Models
from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
