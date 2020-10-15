import numpy


def grid_to_csv_string(grid_schedule):
    csv_string = ""
    for r in grid_schedule:
        for c in r:
            # capitalized_csv_string = ""
            # for word in c.split(" "):
            #     capitalized_csv_string += word.capitalize() + " "
            # if capitalized_csv_string[-1] == " ":
            #     capitalized_csv_string = capitalized_csv_string[:-1]
            # csv_string += str(capitalized_csv_string) + ","
            csv_string += c + ","
        csv_string += "\n"
    return csv_string


def output_csv(csv_string, outfile):
    f = open(outfile, "w")
    f.write(csv_string)
    f.close()


def schedule_to_grid(schedule):
    day_list = [k for k in schedule.keys()]
    max_cols = len(day_list)
    max_rows = 0
    for d in day_list:  # Get biggest day for matrix row bound
        day = schedule[d]
        slot_list = [s for s in day.keys()]
        if len(slot_list) > max_rows:
            max_rows = len(slot_list)

    grid_schedule = numpy.empty(shape=(max_rows+1, max_cols*2), dtype='object')

    j = 0
    for d_i in range(len(day_list)):
        grid_schedule[0,j] = day_list[d_i]
        grid_schedule[0,j+1] = day_list[d_i]
        j += 2

    i = 1
    j = 0
    for d in day_list:
        day = schedule[d]
        slot_list = [s for s in day.keys()]
        for s in slot_list:
            slot = day[s]
            if slot is not None:
                time = slot[0]
                dj = slot[1]

                grid_schedule[i, j] = time
                if dj is not None:
                    grid_schedule[i, j+1] = str(dj)
                else:
                    grid_schedule[i, j+1] = ""
            i += 1
        while i<max_rows+1:
            grid_schedule[i,j] = ""
            grid_schedule[i,j+1] = ""
            i += 1
        i = 1
        j += 2

    return grid_schedule


def output_schedule(schedule, outfile):
    grid = schedule_to_grid(schedule)
    csv_string = grid_to_csv_string(grid)
    # print(csv_string)
    output_csv(csv_string, outfile)
    print("! Finished Outputting Schedule to \"%s\"" % outfile)