from django.contrib import admin

# Model
from centers.models.center import Center
from centers.models.policy import Policy
from centers.models.facility import Facility


class PolicyInline(admin.TabularInline):
    model = Policy.center.through


class FacilityInline(admin.TabularInline):
    model = Facility.center.through


class CenterAdmin(admin.ModelAdmin):
    inlines = [
        PolicyInline,
        FacilityInline,
    ]

admin.site.register(Center, CenterAdmin)
admin.site.register(Policy)
admin.site.register(Facility)
