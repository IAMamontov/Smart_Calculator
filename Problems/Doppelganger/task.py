# the object_list has already been defined
# write your code here

# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
from _collections_abc import Hashable
hash_list = []
hash_dict = {}
c = 0
for item in object_list:
    if isinstance(item, Hashable):
        if hash(item) in hash_dict.keys():
            hash_dict[hash(item)] = hash_dict[hash(item)] + 1
        else:
            hash_dict[hash(item)] = 1
for count in hash_dict.values():
    if count > 1:
        c += count

print(c)
