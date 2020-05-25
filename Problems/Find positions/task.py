# put your python code here
str_out = []
str_in = input().split()
n = input()
for i in range(len(str_in)):
    if str_in[i] == n:
        str_out.append(str(i))
if len(str_out) == 0:
    print("not found")
else:
    print(" ".join(str_out))