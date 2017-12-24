import itertools
x,n=input().split()
[print(''.join(i)) for z in range(1,int(n)+1) for i in itertools.combinations(sorted(x),int(z)) if x.isupper()==True]

