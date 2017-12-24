#!/bin/python3
import sys
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
arr = []
for arr_i in range(n):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
k = int(input().strip())
sorted_table=sorted(arr,key=lambda v:v[k])
for i in sorted_table:
    print(*i)
