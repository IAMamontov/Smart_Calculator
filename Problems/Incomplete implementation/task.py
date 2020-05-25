def startswith_capital_counter(names_in):
    c = 0
    for name in names_in:
        if name[0].isupper():
            c += 1
    return c
