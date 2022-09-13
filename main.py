from pathlib import Path
import sys

import csv_to_schedule as c2s
import csv_to_djs as c2dj
import schedule_to_csv as s2c
import assign_djs_to_slots as ad2s

if __name__ == '__main__':
    # Schedule = {}  # Dictionary of Days of Slots of DJs

    fpath = Path.cwd()  # Current working directly

    dl_sl = c2s.csv_to_days_and_slots(f'{fpath}/sheets/schedule.csv')
    day_list = dl_sl[0]
    slot_list = dl_sl[1]
    Schedule = c2s.build_schedule_from_days_and_slots(day_list, slot_list)
    # print(Schedule)

    dj_list = c2dj.csv_to_dj_list(f'{fpath}/sheets/djs.csv')

    weighted_dj_list = ad2s.build_weighted_list(dj_list)
    Schedule = ad2s.assign_djs(Schedule, weighted_dj_list)

    s2c.output_schedule(Schedule, f'{fpath}/sheets/output_schedule.csv')
    print("All done :)")

    print('Feel free to close the window OR type CTRL+C to exit')
    while True:
        pass
