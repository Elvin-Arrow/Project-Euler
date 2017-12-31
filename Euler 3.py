
i = 2
num = 600851475143
#num = 1000
while i < num:
    if num % i == 0:
        f = 2
        j = 2
        while j < i:
            if i % j == 0:
                f += 1
                break
            j += 1
        if f == 2:
            print(i)
    i += 1

