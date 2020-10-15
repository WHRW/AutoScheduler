import schedule_tools as stools


# Build a sorted list by DJ priority and station service
# TODO: Confirm this actually works ay lmao
def build_weighted_list(dj_list):
    print("! Weighting DJs by Priorities")
    weighted_list = sorted(dj_list, key=lambda dj: (dj.priority, dj.station_service), reverse=True)

    print("Weighted List of DJs:")
    i = 1
    for dj in weighted_list:
        print("\t%d. %s" % (i,dj))
        i += 1
    return weighted_list


# Build schedule using weighted DJ list
def assign_djs(schedule, weighted_dj_list):
    leftover_djs = []
    print("! Assigning DJs to Slots")
    for dj in weighted_dj_list:
        was_given_a_slot = False
        preferred_slots = dj.pref_slots
        for ps in preferred_slots:  # ps is a tuple (day, time)
            ps_day = ps[0]
            ps_time = ps[1]
            if stools.slot_exists(schedule, ps_day, ps_time):
                if stools.slot_is_empty(schedule, ps_day, ps_time):
                    schedule[ps_day][ps_time] = (ps_time, dj)
                    was_given_a_slot = True
                    num_choice = preferred_slots.index(ps)+1
                    print("\tPut %s in (%s, %s), their #%d choice" % (str(dj), ps_day, ps_time ,num_choice))
                    break
        if not was_given_a_slot:
            print("\t!! No slot found for %s" % str(dj))
            leftover_djs.append(dj)

    # print(stools.list_slots(schedule))
    # print(len(stools.list_taken_slots(schedule)))
    # print(len(stools.list_open_slots(schedule)))
    # print(stools.num_slots(schedule))

    schedule = assign_leftover_djs(schedule, leftover_djs)
    return schedule


# Sadly assign DJs who couldn't get slots avoiding ones they absolutely can't do
def assign_leftover_djs(schedule, leftover_list):
    slotless_djs = []
    print("! Assigning %d leftover DJ(s) to Slots" % len(leftover_list))
    for dj in leftover_list:
        was_given_a_slot = False
        barred_slots = dj.barred_slots
        open_slots = stools.list_open_slots(schedule)
        for slot in open_slots:
            if len(barred_slots) == 0 or slot not in barred_slots:
                day = slot[0]
                time = slot[1]
                schedule[day][time] = (time, dj)
                print("\tPut %s in (%s, %s)" % (str(dj), day, time))
                was_given_a_slot = True
                break
        if not was_given_a_slot:
            print("\t!! No possible slots for %s" % str(dj))
            slotless_djs.append(dj)
    if len(slotless_djs) > 0:
        print("! Couldn't place %d DJ(s) into slots" % len(slotless_djs))
        for sdjs in slotless_djs:
            print("\t>",sdjs)
    return schedule
