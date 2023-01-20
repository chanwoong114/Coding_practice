discirmination = lambda x,y,z : x**2 + y**2 == z ** 2

while True:
    x,y,z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    triangle = [x, y, z]

    triangle.sort()

    if discirmination(triangle[0], triangle[1], triangle[2]):
        print('right')
    else:
        print('wrong')