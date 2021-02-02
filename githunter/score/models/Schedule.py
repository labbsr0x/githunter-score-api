import datetime
import mongoengine_goodjson as gj

from mongoengine import StringField, DateTimeField, IntField


class Schedule(gj.Document):

    code = StringField(required=True, unique=True)
    provider = StringField()
    node = StringField()
    interval_type = StringField()
    interval_value = IntField()

    updatedAt = DateTimeField(default=datetime.datetime.now)

    def __init__(
            self,
            code: str,
            provider: str,
            node: str,
            interval_type: str,
            interval_value: int,
            *args,
            **values
    ):
        super().__init__(*args, **values)

        self.code = code
        self.provider = provider
        self.node = node
        self.interval_type = interval_type
        self.interval_value = interval_value
