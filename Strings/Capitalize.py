def capitalize(string):
    for w in string.split():
        string=string.replace(w,w.capitalize())
    return string
