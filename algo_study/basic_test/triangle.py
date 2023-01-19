while True:
    triangle = list(map(int, input().split()))

    if 0 in triangle:
        break

    triangle.sort()

    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
        print('right')
    else:
        print('wrong')
