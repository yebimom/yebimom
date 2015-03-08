from django.test import TestCase, Client
from django.test.utils import override_settings

# Settings
from yebimom.settings.partials import media

# Built-in module
import os
from shutil import rmtree
import urllib2


class CenterImageViewTest(TestCase):
    """
    For saftry purpose, media.TEST_MEDIA_ROOT is used to upload test.
    (after set the media.MEDIA_ROOT value by media.TEST_MEDIA_ROOT)
    """

    def setUp(self):
        # test upload directory
        if not os.path.isdir(media.TEST_MEDIA_ROOT):
            os.mkdir(media.TEST_MEDIA_ROOT)

        # sample file set
        TEST_IMAGE_URL = os.environ['TEST_IMAGE_URL']
        self.file_path = \
            "%s/%s.%s" % (media.TEST_MEDIA_ROOT, 'temp_name', 'png')
        self.f = open(self.file_path, 'w+')
        self.f.write(urllib2.urlopen(TEST_IMAGE_URL).read())
        self.f.seek(0)

        # client
        self.client = Client()
        self.upload_url = '/upload/'

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

    def test_sub_directory_of_media_path_should_be_created_after_upload(self):
        self.client.post(self.upload_url, {'image': self.f})
        self.assertTrue(os.path.isdir(media.TEST_MEDIA_ROOT + '/test/'))


# Settings for Test
CenterImageViewTest = override_settings(
    MEDIA_ROOT=media.TEST_MEDIA_ROOT,
    MEDIA_URL=media.MEDIA_URL
)(CenterImageViewTest)
