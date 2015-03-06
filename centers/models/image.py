from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class CenterImage(models.Model):
    image = ProcessedImageField(
        upload_to='',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
    )
