# Give board 99 hrs, otherwise give what they earned
def calc_station_service(station_service, is_board):
    if is_board:
        return 99
    else:
        return station_service


# Priorities:
#   0 - Community Member w/ <8 Hours
#   1 - Student w/ <8 Hours
#   2 - Community Member w/ >=8 Hours
#   3 - Student w/ >=8 Hours
#   4 - Board
def calc_priority(station_service, is_board, is_community, priority_modifier):
    priority = 0

    if is_board:
        priority = 4

    else:
        if station_service < 8.0:
            if is_community:
                priority = 0
            else:
                priority = 1
        else:
            if is_community:
                priority = 2
            else:
                priority = 3

    priority += priority_modifier / 10.0  # This yields values 0.0 -> 4.9
    return priority


class DJ:

    # DJ Requirements:
    #   Name, Email, ID Card Number
    #   Year, IsCommunity, IsBoard
    #   Station Service
    #   Preferred Slots
    #   Priority Modifier (0->9)
    # Note: All strings are made lowercase
    def __init__(self, name="no dj", email="no email", card_id="0000000000",
                 year="none", is_community=False, is_board=False, station_service=0.0,
                 priority_modifier=0.0, pref_slots=None, barred_slots=None):
        self.name = name.lower()
        self.email = email.lower()
        self.card_id = card_id
        self.year = year.lower()
        self.is_community = is_community
        self.is_board = is_board

        self.station_service = station_service
        if is_board:
            self.station_service = 99

        self.priority = calc_priority(station_service, is_board, is_community, priority_modifier)
        self.pref_slots = pref_slots
        self.barred_slots = barred_slots

    # def __repr__(self):
    #    return self.name

    def __repr__(self):
        capitalized_name = ""
        for word in self.name.split(" "):
            capitalized_name += word.capitalize() + " "
        if capitalized_name[-1] == " ":
            capitalized_name = capitalized_name[:-1]
        return capitalized_name


# Return DJ with more priority
def compare_djs(dj1, dj2):
    if dj1.priority >= dj2.priority:
        return dj1
    else:
        return dj2



