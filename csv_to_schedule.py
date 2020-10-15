import csv


def row_to_slots(row):
    slots = []

    day = row[0]
    for time in row[1:]:  # Ignoring day of the week
        if time == "":  # Ignoring empty time slots
            continue
        slot_temp = (day, time)

        if slot_temp in slots:
            print("!! ERROR: Repeated slot (%s, %s). Recommend checking schedule csv!" % (day, time))
            quit()
        else:
            slots.append(slot_temp)
    return slots


def csv_to_days_and_slots(filename):
    print("! Converting CSV \"%s\" to Slot List" % filename)
    slot_list = []
    day_list = []

    with open(filename, newline='') as djs_csv:
        csv_reader = csv.reader(djs_csv, delimiter=',', quotechar='\"')
        rows = []
        for row in csv_reader:
            rows.append(row)

        for r in rows:
            if r[0] is "":  # Ignores whitespace rows
                continue
            if r[0] in day_list:  # Ignores duplicate rows
                print("!! ERROR: Duplicate day (%s) in CSV input schedule! Recommend deleting." % r[0])
                quit()
            day_list.append(r[0])
            slot_list.extend(row_to_slots(r))

    print('\tFound %d unique slots spanning %d days' % (len(slot_list), len(day_list)))
    for day in day_list:
        print("\t>",day)
    return day_list, slot_list


def build_schedule_from_days_and_slots(day_list, slot_list):
    print("! Building Schedule from Slot List")
    schedule = {}
    for day in day_list:
        slots = {}
        for slot in slot_list:
            if slot[0] == day:
                slots[slot[1]] = (slot[1],None)  # Fill day/slot with no DJ
        schedule[day] = slots
    return schedule
