from django.contrib import admin

# Model
from centers.models.center import Center
from centers.models.policy import Policy
from centers.models.facility import Facility
from centers.models import CenterImage
from centers.models.region import RegionSecondLayer, RegionThirdLayer


class PolicyInline(admin.TabularInline):
    model = Policy.center.through
    classes = ('grp-collapse grp-closed',)


class FacilityInline(admin.TabularInline):
    model = Facility.center.through
    classes = ('grp-collapse grp-closed',)


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


class RegionThirdLayerInline(admin.TabularInline):
    model = RegionThirdLayer
    classes = ('grp-collapse grp-open',)


class RegionAdmin(admin.ModelAdmin):
    inlines = [
        RegionThirdLayerInline,
    ]
    exclude = ('region_first_layer',)


admin.site.register(Center, CenterAdmin)
admin.site.register(RegionSecondLayer, RegionAdmin)
