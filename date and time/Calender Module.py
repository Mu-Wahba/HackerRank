import datetime
x=input()
y=datetime.datetime.strptime(x,'%m %d %Y')
print(datetime.datetime.strftime(y,'%A').upper())
