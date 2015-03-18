def _generate_upload_path(self, file_name):
    return "centers/%s/%s" % (self.center.hash_id, file_name)
