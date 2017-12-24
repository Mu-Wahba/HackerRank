M, N = [set(input().split()) for _ in range(4)][1::2]
c=[print(i) for i in sorted(N.symmetric_difference(M),key=int)]
