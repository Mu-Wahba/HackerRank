N = int(input())
lis=[]
for i in range (0,N):
    com=input().strip().split()  
    if com[0] == 'insert':
        pos=int(com[1])
        val=int(com[2])
        lis.insert(pos,val)
    elif com[0]=='print':
        print(lis)
    elif com[0] == 'remove':
        lis.remove(int(com[1]))
    elif com[0]=='append':
        lis.append(int(com[1]))
    elif com[0] =='sort':
        lis.sort()
    elif com[0]=='pop':
        lis.pop()
    elif com[0]=='reverse':
        lis.reverse()
    elif com[0]=='index':
        lis.index(int(com[1]))
    elif com[0]=='count':
        lis.count(int(lis[1]))
