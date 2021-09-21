import os
from werkzeug.utils import secure_filename

from exceptions.bad_request import BadRequest
from bson.objectid import ObjectId

from repositories import CheckRepository
from models import Check


class CheckService:
    def __init__(self, repository) -> None:
        self.repository: CheckRepository = repository

    def upload(self, args: dict) -> Check:
        # args  = request.files + upload_folder + telegram_id
        if "file" not in args:
            raise BadRequest()

        file = args.get("file")

        if file.filename == "":
            raise BadRequest()

        filename = secure_filename(file.filename)
        path_to_image = os.path.join(args["UPLOAD_FOLDER"], filename)
        file.save(path_to_image)
        check = Check.from_request(args | {"path_to_image": path_to_image})
        check.id = self.repository.create(check)
        return check
