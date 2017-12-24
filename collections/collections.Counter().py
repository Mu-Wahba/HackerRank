##import collections
##x=int(input())
##shoes = collections.Counter(map(int,input().split()[:x]))
##income=0
##for _ in range(int(input())):
##     size,price = map(int,input().split())
##     if shoes[size]:
##          income += price
##          shoes[size] -= 1
##print(income)
##


import itertools
d={}
for i in range(int(input())):
	a,b = map(int,input().split())
	d.setdefault(a,[]).append(b)
print(sum(itertools.chain.from_iterable(d.values())))
print(d)
