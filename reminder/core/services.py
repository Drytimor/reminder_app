"""def record_create(data):
    reminder = Events.objects.create(**data)
    _object = {
        'id': reminder.id,
        'email': reminder.email,
        'datetime': reminder.datetime,
        'time_reminder': reminder.time,
        'message': reminder.message,

    }
    # datetime_form = _object.get('datetime')
    # time = _object.get('time')
    # delta = datetime.timedelta(hours=time)
    # datetime_reminder = datetime_form - delta
    task = task_send_email.delay(_object)
    _object['task_id'] = task.id

    return _object"""