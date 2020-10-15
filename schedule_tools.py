

def list_slots(schedule):
    slots = []
    for d in schedule.keys():
        day = schedule[d]
        for t in day.keys():
            slots.append((d,t))
    return slots


def slot_exists(schedule, day, time):
    if day in schedule.keys():
        d = schedule[day]
        if time in d.keys():
            return True
    return False


def slot_is_empty(schedule, day, time):
    day_slot = schedule[day]
    time_slot = day_slot[time]
    if time_slot[1] is None:
        return True
    return False


def num_slots(schedule):
    count = 0
    for d in schedule.keys():
        day = schedule[d]
        for s in day.keys():
            count += 1
    return count


def list_open_slots(schedule):
    open_slots = []
    for d in schedule.keys():
        day = schedule[d]
        for s in day.keys():
            time = day[s]
            if time[1] is None:
                open_slots.append((d, s))
    return open_slots


def list_taken_slots(schedule):
    taken_slots = []
    for d in schedule.keys():
        day = schedule[d]
        for s in day.keys():
            time = day[s]
            if time[1] is not None:
                taken_slots.append((d, s))
    return taken_slots
