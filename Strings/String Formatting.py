def print_formatted(n):
    w=len(format(n,'b'))
    for i in range(1,n+1):
        print("{0:{we}d} {0:{we}o} {0:{we}X} {0:{we}b}".format(i,we=w))
