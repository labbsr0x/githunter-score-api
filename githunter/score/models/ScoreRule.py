import datetime
import mongoengine_goodjson as gj

from mongoengine import StringField, DateTimeField


class ScoreRule(gj.Document):

    rule_code = StringField()
    name = StringField()
    math = StringField()
    description = StringField()

    updatedAt = DateTimeField(default=datetime.datetime.now)

    def __init__(
            self,
            rule_code: str,
            name: str,
            math: str,
            description: str,
            *args,
            **values
    ):
        super().__init__(*args, **values)

        self.rule_code = rule_code
        self.name = name
        self.math = math
        self.description = description
