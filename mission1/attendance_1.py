from typing import Tuple

id_cnt = 0
GOLD_POINT = 50
SILVER_POINT = 30


def print_grade(name: str, point: int):
    print(f"NAME : {name}, POINT : {point}, GRADE : ", end="")
    if point >= GOLD_POINT:
        print("GOLD")
    elif point >= SILVER_POINT:
        print("SILVER")
    else:
        print("NORMAL")
    return


def add_extra_point(id: int, wed: list, weekend: list):
    extra_point = 0
    if wed[id] >= 10:
        extra_point += 10
    if weekend[id] >= 10:
        extra_point += 10
    return extra_point


def get_id(names_with_id, name):
    global id_cnt
    if name not in names_with_id:
        id_cnt += 1
        names_with_id[name] = id_cnt
    return names_with_id[name]


def print_fail_member(names_with_id: dict, points: list, wed: list, weekend: list):
    print("\nRemoved player")
    print("==============")
    for name, id in names_with_id.items():
        if points[id] < SILVER_POINT and wed[id] == 0 and weekend[id] == 0:
            print(name)


def calculate_all_member_points(attendance_list: list) -> Tuple[dict, list, list, list]:
    names_with_id = {}
    wed = [0] * 100
    weekend = [0] * 100
    points = [0] * 100
    for name, day in attendance_list:
        id = get_id(names_with_id, name)
        points[id] += calculate_points(day)
        set_wed_and_weekend(id, day, wed, weekend)
    return names_with_id, points, wed, weekend


def add_all_member_extra_points(names_with_id: dict, wed: list, weeken: list, points: list):
    for id in names_with_id.values():
        points[id] += add_extra_point(id, wed, weeken)


def print_grade_all_members(names_with_id: dict, points: list):
    for name, id in names_with_id.items():
        print_grade(name, points[id])


def is_wednesday(day: str) -> bool:
    return True if day == "wednesday" else False


def is_weekend(day: str) -> bool:
    return True if day == "saturday" or day == "sunday" else False


def calculate_points(day: str) -> int:
    if is_weekend(day):
        return 2
    elif is_wednesday(day):
        return 3
    return 1


def set_wed_and_weekend(id: int, day: str, wed: list, weekend: list) -> int:
    if is_wednesday(day):
        wed[id] += 1
    elif is_weekend(day):
        weekend[id] += 1
    else:
        pass


def read_attendance_files() -> list:
    attendance_list = []
    with open("attendance_weekday_500.txt", encoding='utf-8') as f:
        for _ in range(500):
            line = f.readline()
            if not line:
                break
            name_and_date = line.strip().split()
            if len(name_and_date) != 2:
                continue
            attendance_list.append(name_and_date)
    return attendance_list


if __name__ == "__main__":
    try:
        attendance_list = read_attendance_files()
        names_with_id, points, wed, weekend = calculate_all_member_points(attendance_list)
        add_all_member_extra_points(names_with_id, wed, weekend, points)
        print_grade_all_members(names_with_id, points)
        print_fail_member(names_with_id, points, wed, weekend)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
