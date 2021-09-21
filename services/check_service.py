import os
from werkzeug.utils import secure_filename

from exceptions.bad_request import BadRequest
from bson.objectid import ObjectId

from repositories import CheckRepository
from models import Check


class CheckService:
    def __init__(self, repository, **utils) -> None:
        self.repository: CheckRepository = repository
        self.img_to_text = utils.get("img_to_text")
        self.check_checker = utils.get("check_checker")

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

        # Todo: Вызвать утилиту для получения информации из картинки
        #  Заполнить инфой модель
