from django.contrib import admin

# Model
from reviews.models import VisitReview, UseReview


admin.site.register(VisitReview)
admin.site.register(UseReview)
