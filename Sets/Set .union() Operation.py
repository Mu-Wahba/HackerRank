En, set1 = int(input()), (map(int, input().strip().split()))
Fr, set2 = int(input()),(map(int, input().strip().split()))

print(len(set(set1) | set(set2)))
