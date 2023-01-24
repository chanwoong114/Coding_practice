# 7 : 강한이름

def get_strong_word(a, b):
    a_count, b_count = 0, 0
    for i in a:
        a_count += ord(i)

    for i in b:
        b_count += ord(i)
    
    if a_count > b_count:
        result = a
    else:
        result = b

    return result

a = 'int'
b = 'float'

print(get_strong_word(a, b))