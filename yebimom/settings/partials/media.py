import os


# Upload path
MEDIA_ROOT = ''
MEDIA_URL = ''


# Test Upload path
TEST_MEDIA_DIR = 'TEST_MEDIA_DIR'

TEST_MEDIA_ROOT = "%s/%s" % (
    os.path.abspath(os.path.dirname(__file__)), TEST_MEDIA_DIR
)

TEST_MEDIA_URL = '/%s/' % TEST_MEDIA_DIR
