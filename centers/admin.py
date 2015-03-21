from django.contrib import admin

# Model
from centers.models.center import Center
from centers.models.policy import Policy
from centers.models.facility import Facility
from centers.models import CenterImage


class PolicyInline(admin.TabularInline):
    model = Policy.center.through


class FacilityInline(admin.TabularInline):
    model = Facility.center.through


class CenterAdmin(admin.ModelAdmin):
    inlines = [
        PolicyInline,
        FacilityInline,
    ]


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(CenterImage)
class CenterImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Center, CenterAdmin)
