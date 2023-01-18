# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 


def group_anagrams(words):
    words_list = {}

    for i in words:
        s = ''.join(sorted(i))
        words_list[s] = words_list.get(s, []) + [i]

    return list(words_list.values())

words = list(map(str, input().split()))

print(group_anagrams(words))