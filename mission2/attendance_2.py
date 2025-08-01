from day_checker import create_day_checker, DayChecker
from person import Person


class Attendance:
    def __init__(self, file: str, day_checker: DayChecker):
        self.id_cnt = 0
        self.persons = {}
        self.attendance_list = []
        self.day_checker = day_checker
        with open(file, encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                name_and_date = line.strip().split()
                if len(name_and_date) != 2:
                    continue
                self.attendance_list.append(name_and_date)

    def make_person(self, name: str) -> Person:
        if name not in self.persons:
            self.id_cnt += 1
            self.persons[name] = Person(name, self.id_cnt)
        return self.persons[name]

    def calculate_all_member_basic_points(self):
        for name, day in self.attendance_list:
            person = self.make_person(name)
            person.calculate_points(day, self.day_checker)
            person.set_special_and_weekend(day, self.day_checker)

    def add_all_member_extra_points(self):
        for person in self.persons.values():
            person.add_extra_point()

    def print_grade_all_members(self):
        for person in self.persons.values():
            person.print_grade()

    def print_fail_member(self):
        print("\nRemoved player")
        print("==============")
        for person in self.persons.values():
            person.print_fail()


def run(file):
    try:
        day_checker = create_day_checker("wednesday")
        attendance = Attendance(file, day_checker)
        attendance.calculate_all_member_basic_points()
        attendance.add_all_member_extra_points()
        attendance.print_grade_all_members()
        attendance.print_fail_member()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        raise FileNotFoundError
