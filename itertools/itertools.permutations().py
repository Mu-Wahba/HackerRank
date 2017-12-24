import itertools
x,n=input().split()
[print(''.join(i)) for i in itertools.permutations(sorted(x),int(n)) if x.isupper()==True]
