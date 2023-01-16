score = {
    'python': 85,
    'django': 89,
    'web': 83,
    'algorithm' : 90
}

total = 0

for i in score:
    total += score[i]


length = len(score)

average = total/length

print(average)