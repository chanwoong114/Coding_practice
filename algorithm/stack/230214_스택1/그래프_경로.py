T = int(input())
for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    adjM = [[] for _ in range(V+1)]
    start, end = map(int, input().split())
    for i in range(E):
        adjM[arr[i][0]].append(arr[i][1])

    visited = [0]*(V+1)
    stack = [start]
    visited[start] = 1

    while stack:
        if stack[-1] == end:
            print(f'#{test_case}', 1)
            break
        for i in adjM[stack[-1]]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

    else:
        print(f'#{test_case}', 0)

