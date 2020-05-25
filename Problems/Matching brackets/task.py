# put your python code here
from collections import deque
def check_brackets(str_in):
    brackets = deque()
    for ch in str_in:
        if ch == "(":
            brackets.append(ch)
        elif ch == ")":
            if len(brackets) == 0:
                return False
            brackets.pop()
    return not bool(len(brackets))


str_ch = input()
if check_brackets(str_ch):
    print("OK")
else:
    print("ERROR")
