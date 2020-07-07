
import os
import base64
from django.views import View

PHOTO_PATH = "/tmp/"


def get_photo_file(self, user_id):
    """
    Gets a photo file (or None)
    """
    file_paths = [{"path": PHOTO_PATH + user_id + ".jpeg",
                   "type": "image/jpeg",
                   "data": None},
                  {"path": PHOTO_PATH + user_id + ".png",
                   "type": "image/png",
                   "data": None}]
    for file_path in file_paths:
        if os.path.exists(file_path["path"]):
            with open(file_path["path"], "rb") as file:
                data = file.read()
                base64_bytes = base64.b64encode(data)
                file_path['data'] = base64_bytes
                return file_path
    return None


class UserPhoto(View):
    def get(self, request, id):
        """ DJANGO Controller Method to return user photo from file
            :param request: http post request
            @Return HttpResponse
        """
        photo = get_photo_file(id)
        return HttpResponse(photo["data"], content_type=photo["type"],
                            status=200)

