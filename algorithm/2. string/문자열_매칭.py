p = 'aa'
t = 'aaaa'
count = 0

def word_check(p ,t):
    if p in t:
        return True
    else: return False

while word_check(p ,t):
    t = t.replace(p, '', 1)
    count += 1

# while word_check(p ,t):

print(len(t)+count)
