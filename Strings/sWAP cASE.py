st=input()
for char in st:
    if char.islower()is True :
        print(char.upper(),end='')

    elif char.isupper()is True :
        print(char.lower(),end='')
    else:
        print(char,end='')
