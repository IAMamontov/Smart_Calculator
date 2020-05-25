# the list "walks" is already defined
# your code here
s = 0
for i in walks:
    s = s + int(i["distance"])
print(s // len(walks))