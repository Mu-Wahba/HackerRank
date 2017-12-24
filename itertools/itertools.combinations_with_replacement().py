import itertools
x,n=input().split()
[print(''.join(i)) for i in itertools.combinations_with_replacement(sorted(x),int(n)) if x.isupper()==True]
