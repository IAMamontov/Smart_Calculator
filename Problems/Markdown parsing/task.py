str_in = input()
table = "*_~`"
new_str = str_in
while len(new_str) >= 1:
    if new_str[0] in table or new_str[len(new_str) - 1] in table:
        c = new_str[0]
        new_str = new_str[1:len(new_str) - 1]
    else:
        break
print(new_str)