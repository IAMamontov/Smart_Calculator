# write your code here
from collections import deque

variables = {}
operators = ["+", "-", "*", "/", "^", "=", "(", ")"]


# print help
# TODO more help
def log_help():
    help_string = "Calculator * / + - with support ^ ( ) and variables. " \
                  "Type /help to see this /exit to exit "
    print(help_string)


# exit
def bye_exit():
    print("Bye!")
    exit(0)


# modify extra + or - like: +++ -> +  -- -> +   --- --> -
def reduce_operator(rough_str):
    n_word = 0
    new_str = []
    while n_word < len(rough_str):
        if rough_str[n_word] == "-":
            c_minus = 1
            i = n_word + 1
            while rough_str[i] == "-":
                c_minus += 1
                i += 1
            if c_minus % 2 == 0:
                new_str.append("+")
            else:
                new_str.append("-")
            n_word = i
        elif rough_str[n_word] == "+":
            i = n_word + 1
            while rough_str[i] == "+":
                i += 1
            else:
                new_str.append("+")
                n_word = i
        else:
            new_str.append(str_in[n_word])
            n_word += 1
    return new_str


# test char is it operator
def is_operator(word):
    return word == "+" or word == "-" \
           or word == "*" or word == "/" or word == "^"


# test precedence of operator
def is_higher_precedence(a, b):
    return (a == "*" or a == "/") and (b == "-" or b == "+") \
           or a == "^" and (b == "-" or b == "+" or b == "/" or b == "*")


# substitute vars with values from dictionary
def substitute_vars(raw_str):
    for i in range(len(raw_str)):
        if raw_str[i].isdecimal():
            continue
        elif raw_str[i].isalpha():
            if raw_str[i] in variables:
                raw_str[i] = variables[raw_str[i]]
            else:
                print("Unknown variable")
                return []
        elif is_operator(raw_str[i][0]):
            if i < len(raw_str[i]) - 1 and raw_str[i][0] == raw_str[i][1]:
                print("Invalid expression")
                return []
        elif raw_str[i] == "=":
            print("Invalid assignment")
            return []
        elif raw_str[i] == "(" or raw_str[i] == ")":
            continue
        else:
            print("Invalid identifier")
            return []
    return raw_str


# assignment procedure with dictionary and test errors with vars and =
def assignment(raw_str):
    if len(raw_str) > 3:
        print("Invalid assignment")
        return
    for word in raw_str[2:]:
        if word == "=":
            print("Invalid assignment")
            return
    if not raw_str[0].isalpha():
        print("Invalid identifier")
    else:
        if raw_str[2].isdecimal():
            variables[raw_str[0]] = raw_str[2]
        elif raw_str[2].isalpha():
            if raw_str[2] not in variables:
                print("Unknown variable")
            else:
                variables[raw_str[0]] = variables[raw_str[2]]
        else:
            print("Invalid assignment")


# test and call command
def extract_command(substr):
    if substr[1:] == "help":
        log_help()
    elif substr[1:] == "exit":
        bye_exit()
    else:
        print("Unknown command")


# covert infix to postfix
def to_postfix(raw_str):
    stack = deque()
    res = []
    for i in raw_str:
        if i.isdecimal():
            res.append(i)
        elif i == "(":
            stack.append(i)
        elif is_operator(i):
            if (len(stack) == 0 or stack[len(stack) - 1] == "(") \
                    or is_higher_precedence(i, stack[len(stack) - 1]):
                stack.append(i)
            else:
                while (len(stack) > 0
                       and (not stack[len(stack) - 1] == "("
                            and not is_higher_precedence(i, stack[len(stack) - 1]))):
                    res.append(stack.pop())
                stack.append(i)
        elif i == ")":
            while len(stack) > 0 and not stack[len(stack) - 1] == "(":
                res.append(stack.pop())
            if len(stack) > 0 and stack[len(stack) - 1] == "(":
                stack.pop()
            else:
                # ( ) error
                return []
    while len(stack) > 0:
        if stack[len(stack) - 1] == "(":
            # ( ) error
            return []
        if stack[len(stack) - 1] == ")":
            # ( ) error
            return []
        else:
            res.append(stack.pop())
    return res


# calculate postfix
def calc_postfix(p_str):
    stack = deque()
    for i in p_str:
        if i.isdecimal():
            stack.append(i)
        elif is_operator(i):
            b = int(stack.pop())
            a = int(stack.pop())
            if i == "+":
                stack.append(a + b)
            elif i == "-":
                stack.append(a - b)
            elif i == "*":
                stack.append(a * b)
            elif i == "/":
                stack.append(a / b)
            elif i == "^":
                stack.append(a ** b)
    return stack.pop()


# main loop
while True:
    str_in = input()
    # empty string back to input
    if len(str_in) == 0:
        continue
    # / means command
    if str(str_in[0]) == "/":
        extract_command(str_in.split()[0])
        continue
    # separate operators with spaces
    for ch in operators:
        str_in = str_in.replace(ch, " " + ch + " ")
    # split string
    str_in = str_in.split()
    # delete extra + or -
    str_in = reduce_operator(str_in)
    # not alone = means assignment or substitute vars
    if len(str_in) > 1 and str_in[1] == "=":
        assignment(str_in)
        continue
    else:
        str_in = substitute_vars(str_in)
        # error inside function back to input
        if not str_in:
            continue
    # one word means display input decimal or var value
    if len(str_in) == 1:
        if str_in[0].isdecimal():
            print(int(str_in[0]))
            continue
        else:
            print("Invalid expression")
            continue
    # two words means error
    elif len(str_in) == 2:
        print("Invalid expression")
        continue
    # more than two words -> convert to postfix and calculate it
    if len(str_in) > 2:
        str_in = to_postfix(str_in)
        if not str_in:
            print("Invalid expression")
            continue
        else:
            print(calc_postfix(str_in))
