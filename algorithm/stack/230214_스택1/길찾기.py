for test_case in range(10):
    t, v = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]

    visited = [0]*100
    start, end = 0, 99
    stack = [1]
    visited[1] = 1

    for i in range(0, v*2, 2):
        graph[arr[i]].append(arr[i+1])

    while stack:
        if stack[-1] == end:
            print(f'#{t}', 1)
            break
        for i in graph[stack[-1]]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                break
        else:
            stack.pop()
    else:
        print(f'#{t}', 0)