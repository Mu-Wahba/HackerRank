n1, set1 = int(input()), set(map(int, input().strip().split()))
n2, set2 = int(input()), set(map(int, input().strip().split()))

print(len(set1 & set2))
