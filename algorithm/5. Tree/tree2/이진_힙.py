def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = heap[1]               # 루트 임시저장
    heap[1]= heap[last]         # 마지막 정점의 값을 루트로 이동
    last -= 1                   # 마지막 정점 삭제
    p = 1
    c = p * 2                   # 왼쪽 자식번호
    while c <= last:            # 자식이 하나 있으면
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1              # 비교 대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]:   # 자식이 부모보다 크면
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2
        else:
            break
    return tmp


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    heap = [0]*(3*n)
    last = 0
    cnt = 0
    for i in lst:
        enq(i)

    while n > 1:
        n //= 2
        cnt += heap[n]

    print(f'#{test_case}', cnt)

