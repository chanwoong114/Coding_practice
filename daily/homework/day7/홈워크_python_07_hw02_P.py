def collatz(n):
    count = 0
    while True:
        if n == 1:
            print(count)
            return 
        if n%2 == 0:
            n = n//2
        elif n%2 == 1:
            n = n*3+1
        count += 1

        if count == 500:
            print(-1)
            return 



collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1