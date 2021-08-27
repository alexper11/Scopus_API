
def read_key():
    with open("key.txt") as key:
        lines = [line.rstrip() for line in key]

    return lines[0], lines[1]
 