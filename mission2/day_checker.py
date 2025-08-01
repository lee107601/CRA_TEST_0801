
WEDNESDAY = "wednesday"


class DayChecker:
    def __init__(self):
        self.special_day = ""
        self.weekend_days = ("saturday", "sunday")

    def is_special_day(self, day: str) -> bool:
        return True if day == self.special_day else False

    def is_weekend(self, day: str) -> bool:
        return True if day in self.weekend_days else False

    def get_day_point(self, day: str) -> int:
        point = 1
        if self.is_weekend(day):
            point = 2
        elif self.is_special_day(day):
            point = 3
        return point


class WednesDayChecker(DayChecker):
    def __init__(self):
        super().__init__()
        self.special_day = "wednesday"


def create_day_checker(special_day: str):
    if special_day == WEDNESDAY:
        return WednesDayChecker()
    else:
        return DayChecker()
