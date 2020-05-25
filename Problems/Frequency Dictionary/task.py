# put your python code here
str_in = input().lower().split()
out = {}
for i in str_in:
    if i not in out.keys():
        out[i] = 1
    else:
        out[i] = out[i] + 1
for i in out:
    print(i, out[i])
