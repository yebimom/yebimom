from centers.models.image import CenterImage

from os.path import splitext

from hashids import Hashids


def _get_center_image_name_hashids():
    return Hashids(salt="sample", min_length=16)


def handle_uploaded_file(f):
    f.name = _encode_center_image_name_hashids(f.name)
    image = CenterImage(image=f)
    image.save()


def _encode_center_image_name_hashids(name):
    hashids = _get_center_image_name_hashids()
    return hashids.encode(1) + splitext(name)[1]
