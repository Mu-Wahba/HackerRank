import itertools
n=input()
#for k,g in itertools.groupby(n):
  # print((len(list(g)),int(k)),end=' ')

print(*[(len(list(g)),int(k)) for k,g in itertools.groupby(n)])
