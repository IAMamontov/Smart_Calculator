from collections import deque

books = deque()
n = int(input())
for _i in range(n):
    str_in = input().split(" ", 1)
    if str_in[0] == "BUY":
        books.append(str_in[1])
    elif str_in[0] == "READ":
        print(books.pop())
    else:
        continue