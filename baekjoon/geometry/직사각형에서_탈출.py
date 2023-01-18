# 1085 : 직사각형에서 탈출
# x,y 입력 받고 w,h 랑 0,0중에 가까운 곳 출력

x, y, w, h = map(int, input().split())

a = [x, y, w-x, h-y]

print(min(a))