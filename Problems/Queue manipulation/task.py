from collections import deque
queue = deque()
n = int(input())
for _i in range(n):
    str_in = input().split()
    if str_in[0] == "ENQUEUE":
        queue.appendleft(str_in[1])
    elif str_in[0] == "DEQUEUE":
        queue.pop()
for _i in range(len(queue)):
    print(queue.pop())