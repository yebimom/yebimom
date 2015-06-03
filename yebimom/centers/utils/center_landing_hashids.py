from hashids import Hashids
from yebimom.settings.partials.application import HASHIDS_CENTER_LANDING_SALT


def get_center_landing_hashids_object():
    return Hashids(salt=HASHIDS_CENTER_LANDING_SALT, min_length=6)


def get_encoded_center_landing_hashid(center_id):
    hashids = get_center_landing_hashids_object()
    return hashids.encode(center_id)


def get_decoded_center_landing_hashid(center_hash_id):
    hashids = get_center_landing_hashids_object()
    return hashids.decode(center_hash_id)[0]
