studentList= []
for i in range(int(input())):
    name = input()
    score = float(input())
    studentList.append([name, score])
scoreSort = sorted({s[1] for s in studentList})
nameSort = sorted(s[0] for s in studentList if s[1] == scoreSort[1])
print(*nameSort,sep='\n')
