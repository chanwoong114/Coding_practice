


def solution(bakery_schedule, current_time, k):
    hour, minute = int(current_time[:2]), int(current_time[3:])
    answer = 0
    for i in bakery_schedule:
        b_hour = int(i[:2])
        b_minute = int(i[3:5])
        bread = int(i[6:])

        if b_hour > hour:
            k -= bread
            if b_minute >= minute:
                answer += 60*(b_hour - hour) + (b_minute - minute)
                hour = b_hour
                minute =b_minute
            else:
                answer += 60*((b_hour-1) - hour) + ((b_minute+60) - minute)
                hour = b_hour
                minute = b_minute

        elif b_hour == hour:
            if b_minute >= minute:
                k -= bread
                answer += b_minute - minute
                hour = b_hour
                minute = b_minute

        if k <= 0:
            break

    if k > 0:
        answer = -1

    return answer

print(solution(["09:05 10", "12:20 5", "13:25 6", "14:24 5"], "12:05", 10))
print(solution(["12:00 10"], "12:00", 10))
print(solution(["12:00 10"], "12:00", 11))