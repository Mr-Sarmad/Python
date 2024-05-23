l=[1,5,6,9,8]
print(l)
l.append(9)
# list k end mn kuch add krny k liye y function use hta h
print(l)
l.sort()
# list k asscending order mn print krny k liye y use hta h 
print(l)
l.sort(reverse=True)
# list k decending order mn print krny k liye use hta h 
print(l)
l.reverse()
# jo original list usko reverse kr deta h
print(l)
print(l.count(9))
# list mn sy given value k cout krny k liye 
print(l.index(9))
# list mn sy given value k index maloom krny k liye 
m=l.copy()
# l k content m mn copy krny k liye hm is function ka use krty h 
m[0]=86
print(l)
print(m)
m.insert(3,789)
# list mn index mn value k chnge krny k liye hm is fun k use krty hn
print(m)
j=[1000,5000,890000]
m.extend(j)
# list k end mn kuch add krny k liye use hta h 
print(m)
k=l+m
# the list k add krny k liye 
print(k)
