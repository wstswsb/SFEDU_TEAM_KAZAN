import os
import json
from werkzeug.utils import secure_filename

from exceptions.bad_request import BadRequest
from bson.objectid import ObjectId

from repositories import CheckRepository
from models import Check

from utils import (
    ImgToText,
    CheckChecker
)
from loggers_factory import loggers_factory


class CheckService:
    def __init__(self, repository, **utils) -> None:
        self.repository: CheckRepository = repository
        self.img_to_text: ImgToText = utils.get("img_to_text")
        self.check_checker: CheckChecker = utils.get("check_checker")
        self.logger = loggers_factory.get()

    def upload(self, args: dict) -> Check:
        # args  = request.files + upload_folder + telegram_id
        """
            {
                // request.files,
                "UPLOAD_FOLDER": str,
                "telegram_img_id: str
                "telegram_owner_id": str
            }
        """
        args["path_to_img"] = self._save_image(args)
        args["text"] = self.img_to_text.translate(
            args['path_to_img']).decode().upper()
        print(args["text"])
        self.logger.debug(args)
        if not self.check_checker.is_check(args["text"]):
            self.logger.debug("no keywords in text")
            raise BadRequest()

        check = Check()
        check.assign_request(args)
        self.logger.debug(check)
        self.repository.create(check)
        return check

    def _save_image(self, args: dict) -> str:
        if "file" not in args:
            raise BadRequest()
        file = args.get("file")
        filename = secure_filename(file.filename)
        path_to_image = os.path.join(args["UPLOAD_FOLDER"], filename)
        file.save(path_to_image)
        return path_to_image
