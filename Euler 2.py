first = 0
second = 1
n_sum = 0
while second < 4000000:
    next_n = first + second
    first = second
    second = next_n
    if next_n % 2 == 0:
        n_sum += next_n
print(n_sum)
