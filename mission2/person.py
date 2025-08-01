from day_checker import DayChecker
GOLD_POINT = 50
SILVER_POINT = 30


class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.special = 0
        self.weekend = 0
        self.point = 0

    def add_extra_point(self):
        extra_point = 0
        if self.special >= 10:
            extra_point += 10
        if self.weekend >= 10:
            extra_point += 10
        self.point += extra_point

    def calculate_points(self, day: str, day_checker: DayChecker):
        self.point += day_checker.get_day_point(day)

    def set_special_and_weekend(self, day: str, day_checker: DayChecker) -> int:
        if day_checker.is_special_day(day):
            self.special += 1
        elif day_checker.is_weekend(day):
            self.weekend += 1
        else:
            pass

    def print_grade(self):
        print(f"NAME : {self.name}, POINT : {self.point}, GRADE : ", end="")
        if self.point >= GOLD_POINT:
            print("GOLD")
        elif self.point >= SILVER_POINT:
            print("SILVER")
        else:
            print("NORMAL")
        return

    def print_fail(self):
        if self.point < SILVER_POINT and self.special == 0 and self.weekend == 0:
            print(self.name)