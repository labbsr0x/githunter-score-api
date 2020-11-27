import datetime
import mongoengine_goodjson as gj

from mongoengine import StringField, DateTimeField, IntField, FloatField
from githunter.score.utils.score_util import get_ruler


class Score(gj.Document):

    score = FloatField()
    name = StringField()
    user = StringField()
    owner = StringField()
    thing = StringField()
    node = StringField()
    scheduler_code = StringField()
    ruler = IntField()
    stars_received = IntField()
    commits = IntField()
    pull_requests = IntField()
    issues_opened = IntField()
    contributed_repositories = IntField()

    updatedAt = DateTimeField(default=datetime.datetime.now)

    def __init__(
            self,
            score: float,
            name: str,
            user: str,
            owner: str,
            thing: str,
            node: str,
            scheduler_code: str,
            stars_received: int,
            commits: int,
            pull_requests: int,
            issues_opened: int,
            contributed_repositories: int,
            *args,
            **values
    ):
        super().__init__(*args, **values)

        self.score = score
        self.ruler = get_ruler(score)
        self.name = name
        self.user = user
        self.owner = owner
        self.thing = thing
        self.node = node
        self.scheduler_code = scheduler_code
        self.stars_received = stars_received
        self.commits = commits
        self.pull_requests = pull_requests
        self.issues_opened = issues_opened
        self.contributed_repositories = contributed_repositories
