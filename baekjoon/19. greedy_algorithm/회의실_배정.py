n = int(input())

conference = [list(map(int, input().split())) for _ in range(n)]

conference.sort(key = lambda x:(x[1], x[0]))

cnt = 1
end_conference = conference[0][1]
for i in range(1, n):
    if conference[i][0] >= end_conference:
        cnt += 1
        end_conference = conference[i][1]

print(cnt)