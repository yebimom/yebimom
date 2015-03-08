from centers.models.image import CenterImage

from os.path import splitext

from hashids import Hashids


def get_center_image_name_hashids():
    return Hashids(salt="sample", min_length=16)


def handle_uploaded_file(f):
    f.name = encode_center_image_name_hashids(f.name)
    image = CenterImage(image=f)
    image.save()


def encode_center_image_name_hashids(name):
    hashids = get_center_image_name_hashids()
    return hashids.encode(1) + splitext(name)[1]
