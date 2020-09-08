from mongoengine import NotUniqueError
from githunter.score.models.Schedule import Schedule
from githunter.score.utils.response_util import get_response, get_success
from githunter.score.utils.string_util import clean
from githunter.score import scheduler


def create_new(data: {}) -> {}:
    owner = data['owner']
    thing = data['thing']
    node = data['node']
    interval_type = data['interval_type']
    interval_value = data['interval_value']
    code = clean(owner + thing + node)

    schedule = Schedule(
        code,
        owner,
        thing,
        node,
        interval_type,
        interval_value
    )

    try:
        if interval_value > 0:
            saved = schedule.save()
            scheduler.add(saved)
            return get_success(saved.to_json())
        else:
            scheduler.add(schedule)
            return get_success(schedule.to_json())

    except NotUniqueError as e:
        return get_response(409, "SCHEDULE_ALREADY_EXISTS", None, e)
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def get_all():
    try:
        all_schedules = Schedule.objects()
        return get_success(all_schedules.to_json())
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def remove(code: str):
    try:
        removed = Schedule.objects(code=code).delete()
        if removed > 0:
            scheduler.remove(code)
            return get_success()
        return get_response(404, "SCHEDULE_ITEM_NOT_FOUND")
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def get_by_code(code: str):
    try:
        items = Schedule.objects(code=code)
        if len(items) > 0:
            return get_success(items[0].to_json())
        return get_response(404, "SCHEDULE_ITEM_NOT_FOUND")
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)
