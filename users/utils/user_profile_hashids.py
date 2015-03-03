from yebimom.settings.partials.application import HASHIDS_USER_PROFILE_SALT
from hashids import Hashids


# Hashids
def get_user_profile_hashids():
    return Hashids(salt=HASHIDS_USER_PROFILE_SALT, min_length=16)


def encode_user_profile_hashids(userprofile_id):
    hashids = get_user_profile_hashids()
    return hashids.encode(userprofile_id)


def decode_user_profile_hashids(userprofile_hash_id):
    hashids = get_user_profile_hashids()
    return hashids.decode(userprofile_hash_id)[0]
