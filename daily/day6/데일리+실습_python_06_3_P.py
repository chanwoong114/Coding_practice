vowels = ['a','e','i','o','u']

def count_vowels(s):
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    
    print(count)
    return 

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3