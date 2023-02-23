# # 최대 힙
# def enq(n):
#     global last
#     last += 1  # 완전이진트리에 마지막 정점을 추가하고
#     heap[last] = n  # 마지막 정점에 저장
#     c = last  # 부모가 있고, 부모 > 자식
#     p = c // 2
#     while p > 0 and heap[p] < heap[c]:
#         heap[p], heap[c] = heap[c], heap[p]
#         c = p  # 옮긴 자리에서 부모와 비교하기 위해
#         p = c // 2
#     return
#
#
# heap = [0] * 101
# last = 0
# enq(5)
# print(heap[1])
# enq(15)
# print(heap[1])
# enq(8)
# print(heap[1])
# enq(20)
# print(heap[1])
#
# def deq():
#     global last
#     tmp = heap[1]               # 루트 임시저장
#     heap[1]= heap[last]         # 마지막 정점의 값을 루트로 이동
#     last -= 1                   # 마지막 정점 삭제
#     p = 1
#     c = p * 2                   # 왼쪽 자식번호
#     while c <= last:            # 자식이 하나 있으면
#         if c+1 <= last and heap[c] < heap[c+1]:
#             c += 1              # 비교 대상을 오른쪽 자식으로 변경
#         if heap[c] > heap[p]:   # 자식이 부모보다 크면
#             heap[c], heap[p] = heap[p], heap[c]
#             p = c
#             c = p * 2
#         else:
#             break
#     return tmp
#
# while last>1:
#     print(deq())
#
#
# def insert(item):
#     pos = 1
#     while tree[pos] != 0:
#         if tree[pos] < item:
#             pos = pos*2 +1
#         else:
#             pos = pos*2
#
#     tree[pos] = item
#
# def find(key):
#     pos = 1
#     while tree[pos] != 0:
#         if tree[pos] == key:
#             return pos
#         if tree[pos] < key:
#             pos = pos*2 + 1
#         else:
#             pos = pos*2
#     return -1
#
# tree = [0]*100
# lst = [9, 4, 12, 3, 6, 15, 13, 17]
# for item in lst:
#     insert(item)
#     print(tree)
#
# insert(5)
# print(tree)
# print(find(12))
# print(find(17))
# print(find(3))
# print(find(2))
# print(find(20))
# print(find(7))

# import heapq
#
# h = []
# lst = [15, 4, 13, 20, 11, 19]
# for item in lst:
#     heapq.heappush(h, item)
#
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))

def enq(item):
    global last
    last += 1
    tree[last] = item
    c = last
    p = c//2
    while p > 0 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2
    return

def deq():
    tmp = tree[1]
    tree[1] = tree[last]
    p = 1
    # if tree[p*2] > tree[p*2+1]:
    #     c = p*2
    # else:
    #     c = p*2 + 1
    c = p * 2
    while c <= last: # 자식 노드가 하나라도 있는동안
        if c+1 <= last and tree[c] < tree[c+1]:
            c += 1
        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break

    return tmp



tree = [0] * 100
lst = [15, 4, 13, 20, 11, 19]
last = 0
for item in lst:
    enq(item)