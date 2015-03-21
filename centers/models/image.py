from django.db import models

# utils
from centers.utils.image_handling import _generate_upload_path


class CenterImage(models.Model):
    center = models.ForeignKey('Center')

    image = models.ImageField(upload_to=_generate_upload_path)
