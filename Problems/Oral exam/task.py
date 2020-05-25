from collections import deque
students = deque()
n = int(input())
for _i in range(n):
    str_in = input().split()
    if str_in[0] == "READY":
        students.appendleft(str_in[1])
    elif str_in[0] == "PASSED":
        print(students.pop())
    elif str_in[0] == "EXTRA":
        students.appendleft(students.pop())