for test_case in range(1, 11):
    tc, m = map(int, input().split())
    graph = [[] for _ in range(100)]

    line = list(map(int, input().split()))
    for i in range(0, m*2, 2):
        graph[line[i]].append(line[i+1])

    st = [0]
    visited = [0]*100
    visited[0] = 1

    def dfs():
        while st:
            if st[-1] == 99:
                print(1)
                break

            for i in graph[st[-1]]:
                if not visited[i]:
                    visited[i] = 1
                    st.append(i)
                    break
            else:
                st.pop()
        else:
            print(0)
    flag = 0
    def dfs2(n):
        global flag
        if n == 99:
            flag = 1
            return

        for i in graph[n]:
            if not visited[i]:
                visited[i] = 1
                dfs2(i)

    dfs2(0)

    print(flag)