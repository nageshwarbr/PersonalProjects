from collections import Counter
lst=[1,2,3,4,5,1,2,4,4,4,5]
cnt=Counter(lst)
print(cnt)
print(cnt[1])
print(list(cnt.elements()))
print(cnt.get(7))
print(cnt.most_common(3))
# help(cnt)


