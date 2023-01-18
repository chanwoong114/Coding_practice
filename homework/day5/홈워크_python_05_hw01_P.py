# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
import calendar


def leap_year(n):
    if n%4 == 0:
        if n%100 == 0:
            if n%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

while True:
    year = int(input())
    if leap_year(year):
        print('윤년입니다, 연도를 다시 입력해주세요.')
        continue
    else:
        print(calendar.calendar(year))
        break

month = int(input())
day = int(input())

calendar.day_name(2023, 8, 31)