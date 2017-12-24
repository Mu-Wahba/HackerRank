from itertools import combinations

N,s,n = int(input()),input().split(),int(input())
t = list(combinations(s[:N],n))
f = [i for i in t if 'a' in i]
print(len(f)/len(t))
