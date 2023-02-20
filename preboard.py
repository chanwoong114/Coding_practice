T = 10
for test_case in range(1, T+1):
    t, v = map(int, input().split())
    ll = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visit = [0]*100

    for i in range(v):
        graph[ll[i*2]].append(ll[i*2+1])

    st = [0]
    visit[0] = 1

    while st:
        if st[-1] == 99:
            print(f'#{test_case}', 1)
            break

        for i in graph[st[-1]]:
            if not visit[i]:
                visit[i] = 1
                st.append(i)
                break
        else:
            st.pop()

    else:
        print(f'#{test_case}', 0)