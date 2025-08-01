from mission2.attendance_2 import run
import sys
import pytest
import io


def test_success():
    buffer = io.StringIO()
    sys.stdout = buffer
    file = "attendance_weekday_500.txt"
    run(file)
    sys.stdout = sys.__stdout__
    a = buffer.getvalue()
    assert a== 'NAME : Umar, POINT : 48, GRADE : SILVER\nNAME : Daisy, POINT : 45, GRADE : SILVER\nNAME : Alice, POINT : 61, GRADE : GOLD\nNAME : Xena, POINT : 91, GRADE : GOLD\nNAME : Ian, POINT : 23, GRADE : NORMAL\nNAME : Hannah, POINT : 127, GRADE : GOLD\nNAME : Ethan, POINT : 44, GRADE : SILVER\nNAME : Vera, POINT : 22, GRADE : NORMAL\nNAME : Rachel, POINT : 54, GRADE : GOLD\nNAME : Charlie, POINT : 58, GRADE : GOLD\nNAME : Steve, POINT : 38, GRADE : SILVER\nNAME : Nina, POINT : 79, GRADE : GOLD\nNAME : Bob, POINT : 8, GRADE : NORMAL\nNAME : George, POINT : 42, GRADE : SILVER\nNAME : Quinn, POINT : 6, GRADE : NORMAL\nNAME : Tina, POINT : 24, GRADE : NORMAL\nNAME : Will, POINT : 36, GRADE : SILVER\nNAME : Oscar, POINT : 13, GRADE : NORMAL\nNAME : Zane, POINT : 1, GRADE : NORMAL\n\nRemoved player\n==============\nBob\nZane\n'



def test_file_not_found():
    file = "attendance_weekday_5001.txt"
    with pytest.raises(FileNotFoundError):
        run(file)



def test_500_over():
    buffer = io.StringIO()
    sys.stdout = buffer
    file = "attendance_weekday_502.txt"
    run(file)
    sys.stdout = sys.__stdout__
    a = buffer.getvalue()
    assert a== 'NAME : Umar, POINT : 48, GRADE : SILVER\nNAME : Daisy, POINT : 45, GRADE : SILVER\nNAME : Alice, POINT : 61, GRADE : GOLD\nNAME : Xena, POINT : 91, GRADE : GOLD\nNAME : Ian, POINT : 23, GRADE : NORMAL\nNAME : Hannah, POINT : 127, GRADE : GOLD\nNAME : Ethan, POINT : 44, GRADE : SILVER\nNAME : Vera, POINT : 22, GRADE : NORMAL\nNAME : Rachel, POINT : 54, GRADE : GOLD\nNAME : Charlie, POINT : 58, GRADE : GOLD\nNAME : Steve, POINT : 38, GRADE : SILVER\nNAME : Nina, POINT : 79, GRADE : GOLD\nNAME : Bob, POINT : 8, GRADE : NORMAL\nNAME : George, POINT : 42, GRADE : SILVER\nNAME : Quinn, POINT : 6, GRADE : NORMAL\nNAME : Tina, POINT : 24, GRADE : NORMAL\nNAME : Will, POINT : 36, GRADE : SILVER\nNAME : Oscar, POINT : 13, GRADE : NORMAL\nNAME : Zane, POINT : 1, GRADE : NORMAL\n\nRemoved player\n==============\nBob\nZane\n'


def test_3_words():
    buffer = io.StringIO()
    sys.stdout = buffer
    file = "attendance_weekday_503.txt"
    run(file)
    sys.stdout = sys.__stdout__
    a = buffer.getvalue()
    assert a== 'NAME : Umar, POINT : 48, GRADE : SILVER\nNAME : Daisy, POINT : 45, GRADE : SILVER\nNAME : Alice, POINT : 61, GRADE : GOLD\nNAME : Xena, POINT : 91, GRADE : GOLD\nNAME : Ian, POINT : 23, GRADE : NORMAL\nNAME : Hannah, POINT : 127, GRADE : GOLD\nNAME : Ethan, POINT : 44, GRADE : SILVER\nNAME : Vera, POINT : 22, GRADE : NORMAL\nNAME : Rachel, POINT : 54, GRADE : GOLD\nNAME : Steve, POINT : 38, GRADE : SILVER\nNAME : Nina, POINT : 79, GRADE : GOLD\nNAME : Bob, POINT : 8, GRADE : NORMAL\nNAME : Charlie, POINT : 57, GRADE : GOLD\nNAME : George, POINT : 42, GRADE : SILVER\nNAME : Quinn, POINT : 6, GRADE : NORMAL\nNAME : Tina, POINT : 24, GRADE : NORMAL\nNAME : Will, POINT : 36, GRADE : SILVER\nNAME : Oscar, POINT : 13, GRADE : NORMAL\nNAME : Zane, POINT : 1, GRADE : NORMAL\n\nRemoved player\n==============\nBob\nZane\n'



def test_500_under():
    buffer = io.StringIO()
    sys.stdout = buffer
    file = "attendance_weekday_504.txt"
    run(file)
    sys.stdout = sys.__stdout__
    a = buffer.getvalue()
    assert a=='NAME : Charlie, POINT : 56, GRADE : GOLD\nNAME : Umar, POINT : 44, GRADE : SILVER\nNAME : Hannah, POINT : 122, GRADE : GOLD\nNAME : Steve, POINT : 36, GRADE : SILVER\nNAME : Rachel, POINT : 51, GRADE : GOLD\nNAME : Nina, POINT : 77, GRADE : GOLD\nNAME : Will, POINT : 33, GRADE : SILVER\nNAME : Daisy, POINT : 43, GRADE : SILVER\nNAME : Vera, POINT : 21, GRADE : NORMAL\nNAME : Tina, POINT : 23, GRADE : NORMAL\nNAME : Xena, POINT : 85, GRADE : GOLD\nNAME : Alice, POINT : 57, GRADE : GOLD\nNAME : George, POINT : 40, GRADE : SILVER\nNAME : Ethan, POINT : 44, GRADE : SILVER\nNAME : Oscar, POINT : 13, GRADE : NORMAL\nNAME : Ian, POINT : 19, GRADE : NORMAL\nNAME : Quinn, POINT : 5, GRADE : NORMAL\nNAME : Bob, POINT : 8, GRADE : NORMAL\nNAME : Zane, POINT : 1, GRADE : NORMAL\n\nRemoved player\n==============\nBob\nZane\n'