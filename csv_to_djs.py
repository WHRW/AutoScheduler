import csv
import dj


# "Monday 3:00" --> ("Monday","3:00")
def slots_to_list(slots_str):
    slots = []
    slots_str_list = slots_str.split(",")
    for slot_str in slots_str_list:
        if slot_str[0] == " ":  # Remove leading spaces
            slot_str = slot_str[1:]

        split_slot = slot_str.split(" ")
        final_slot = (split_slot[0], split_slot[1])
        slots.append(final_slot)
    return slots


def row_to_dj(row, row_id):

    if len(row) < 8:
        print("!! ERROR: In Row %d, Missing DJ's information. Recommend checking DJs csv!" % row_id)
        quit()

    name = row[0].lower()  # Lowercase, just in case (BARS)
    if name[-1] == " ":  # Remove space at end of name, if it exists
        name = name[:-1]  # Not even super necessary but JUST IN CASE

    email = row[1]
    card_id = row[2]
    year = row[3]
    is_community = (True if row[4] == "TRUE" else False)
    is_board = (True if row[5] == "TRUE" else False)
    station_service = float(row[6])
    priority_modifier = float(row[7])

    preferred_slots = row[8]
    barred_slots = row[9]

    if preferred_slots is not "":
        preferred_slots = slots_to_list(preferred_slots)
    if barred_slots is not "":
        barred_slots = slots_to_list(barred_slots)

    return dj.DJ(name, email, card_id, year, is_community, is_board,
                 station_service, priority_modifier, preferred_slots, barred_slots)


def csv_to_dj_list(filename):
    print("! Converting CSV \"%s\" to DJ List" % filename)
    dj_names = []
    dj_list = []
    with open(filename, newline='') as djs_csv:
        csv_reader = csv.reader(djs_csv, delimiter=',', quotechar='\"')
        rows = []
        for row in csv_reader:
            rows.append(row)

        r_id = 1
        for r in rows[1:]:  # Ignore row headers
            new_dj = row_to_dj(r, r_id)
            print("\tFound new DJ: %s, SS: %f, Priority: %f" % (new_dj, new_dj.station_service, new_dj.priority))

            if new_dj.name in dj_names:
                print("!! ERROR: In Row %d, Repeated DJ (%s). Recommend checking DJs csv!" % (r_id, new_dj.name))
                quit()
            else:
                dj_list.append(new_dj)
                dj_names.append(new_dj.name)
            r_id += 1
    return dj_list

