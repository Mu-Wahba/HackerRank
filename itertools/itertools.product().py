from itertools import product
a=map(int,input().split())
b=map(int,input().split())

#[print( i ,end=' ') for i in list(product(a,b))]
print(*list(product(a,b)))
