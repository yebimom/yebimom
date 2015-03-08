from django.db import models

# Django 3rd Party Modules
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# utils
from centers.utils.handle_upload_path import _generate_upload_path


class CenterImage(models.Model):
    image = ProcessedImageField(
        upload_to=_generate_upload_path,
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
    )
