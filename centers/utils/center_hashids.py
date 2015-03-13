from hashids import Hashids
from yebimom.settings.partials.application import HASHIDS_CENTER_SALT


def get_center_hashids_object():
    return Hashids(salt=HASHIDS_CENTER_SALT, min_length=5)


def get_encoded_center_hashid(center_id):
    hashids = get_center_hashids_object()
    return hashids.encode(center_id)


def get_decoded_center_hashid(center_hash_id):
    hashids = get_center_hashids_object()
    return hashids.decode(center_hash_id)[0]
