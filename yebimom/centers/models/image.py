from django.db import models


def _generate_upload_path(self, file_name):
    return "centers/%s/%s" % (self.center.hash_id, file_name)


class CenterImage(models.Model):
    center = models.ForeignKey('Center')

    image = models.ImageField(upload_to=_generate_upload_path)
    is_main = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (self.center.name, self.image.name)
