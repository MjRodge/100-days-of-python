def add(*args):
    total = 0
    for n in args:
        total += n
    return total


total_args = add(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(total_args)
