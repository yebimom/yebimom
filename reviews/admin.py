from django.contrib import admin

# Model
from reviews.models import VisitReview, ExperienceReview


admin.site.register(VisitReview)
admin.site.register(ExperienceReview)
