import datetime
import mongoengine_goodjson as gj

from mongoengine import StringField, DateTimeField, IntField, FloatField
from githunter.score.utils.score_util import get_ruler


class Score(gj.Document):

    score = FloatField()
    user = StringField()
    owner = StringField()
    thing = StringField()
    node = StringField()
    scheduler_code = StringField()
    ruler = IntField()

    updatedAt = DateTimeField(default=datetime.datetime.now)

    def __init__(
            self,
            score: float,
            user: str,
            owner: str,
            thing: str,
            node: str,
            scheduler_code: str,
            *args,
            **values
    ):
        super().__init__(*args, **values)

        self.score = score
        self.ruler = get_ruler(score)
        self.user = user
        self.owner = owner
        self.thing = thing
        self.node = node
        self.scheduler_code = scheduler_code
