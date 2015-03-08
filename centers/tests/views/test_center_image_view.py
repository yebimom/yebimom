from django.test import TestCase

# Form
# from centers.forms.center_image_form import CenterImageForm

# settings
from yebimom.settings.partials import media

# built-in module
import os
from shutil import rmtree


class CenterImageViewTest(TestCase):
    """
    For saftry purpose, media.TEST_MEDIA_ROOT is used to upload test.
    (after set the media.MEDIA_ROOT value by media.TEST_MEDIA_ROOT)
    """

    def setUp(self):
        media.MEDIA_ROOT = media.TEST_MEDIA_ROOT
        media.MEDIA_URL = media.TEST_MEDIA_URL

        if not os.path.isdir(media.TEST_MEDIA_ROOT):
            os.mkdir(media.TEST_MEDIA_ROOT)

        file_name = "%s/%s.%s" % (media.MEDIA_ROOT, "temp_name", "jpg")
        self.f = open(file_name, 'w')

    def tearDown(self):
        if os.path.isdir(media.TEST_MEDIA_ROOT):
            rmtree(media.TEST_MEDIA_ROOT)

    def test_media_directory_should_not_exist_after_rmtree(self):
        rmtree(media.TEST_MEDIA_ROOT)
        self.assertFalse(
            os.path.isfile(media.TEST_MEDIA_ROOT)
        )

    def test_setup_should_create_media_directory(self):
        self.assertTrue(
            os.path.isdir(media.TEST_MEDIA_ROOT)
        )
