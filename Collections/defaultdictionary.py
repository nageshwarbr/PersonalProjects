from collections import defaultdict

# The defaultdict works exactly like a python dictionary, except for it does not throw KeyError when you try to access a
# non-existent key.

nums = defaultdict(int)
nums['A'] = 1
nums['B'] = 2
print(nums['C'])  # 0 printed

# count of each name in a list of names given as
# "Mike, John, Mike, Anna, Mike, John, John, Mike, Mike, Britney, Smith, Anna, Smith".
count = defaultdict(int)
str = "Mike, John, Mike, Anna, Mike, John, John, Mike, Mike, Britney, Smith, Anna, Smith"
names_list = str.split(',')
for names in names_list:
    count[names] += 1
print(count)
# help(defaultdict)
