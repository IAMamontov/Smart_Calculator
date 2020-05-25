def range_sum(numbers_in, aa, bb):
    s = 0
    for i in numbers_in:
        if aa <= i <= bb:
            s += i
    return s


numbers = map(int, input().split())
a, b = map(int, input().split())
print(range_sum(numbers, a, b))
