import datetime
import mongoengine_goodjson as gj

from mongoengine import StringField, DateTimeField, IntField


class Schedule(gj.Document):

    code = StringField(required=True, unique=True)
    interval_type = StringField()
    interval_value = IntField()

    updatedAt = DateTimeField(default=datetime.datetime.now)

    def __init__(
            self,
            code: str,
            interval_type: str,
            interval_value: int,
            *args,
            **values
    ):
        super().__init__(*args, **values)

        self.code = code
        self.interval_type = interval_type
        self.interval_value = interval_value
