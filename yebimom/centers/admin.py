from django.contrib import admin

# Model
from centers.models.center import Center
from centers.models.policy import Policy
from centers.models.facility import Facility
from centers.models import CenterImage
from centers.models.region import RegionSecondLayer, RegionThirdLayer
from centers.models.category import Category
from centers.models.center_landing import CenterLanding
from centers.models.center_contact import CenterContact

# Translation
from modeltranslation.admin import TranslationAdmin


class PolicyInline(admin.TabularInline):
    model = Policy.center.through
    classes = ('grp-collapse grp-closed',)


class FacilityInline(admin.TabularInline):
    model = Facility.center.through
    classes = ('grp-collapse grp-closed',)


class CategoryInline(admin.TabularInline):
    model = Category.centers.through
    classes = ('grp-collapse grp-closed',)


class CenterAdmin(admin.ModelAdmin):
    inlines = [
        PolicyInline,
        FacilityInline,
        CategoryInline,
    ]


class CenterTranslationAdmin(CenterAdmin, TranslationAdmin):
    pass


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(CenterImage)
class CenterImageAdmin(admin.ModelAdmin):
    pass


@admin.register(CenterLanding)
class CenterLandingAdmin(admin.ModelAdmin):
    pass


@admin.register(CenterContact)
class CenterContactAdmin(admin.ModelAdmin):
    pass


class RegionThirdLayerInline(admin.TabularInline):
    model = RegionThirdLayer
    classes = ('grp-collapse grp-open',)


class RegionAdmin(admin.ModelAdmin):
    inlines = [
        RegionThirdLayerInline,
    ]
    exclude = ('region_first_layer',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Center, CenterTranslationAdmin)
admin.site.register(RegionSecondLayer, RegionAdmin)
