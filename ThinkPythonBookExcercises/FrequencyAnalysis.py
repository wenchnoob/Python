

def read_file(name):
    ls = []
    with open(name, 'r') as file:
        for line in file:
            ls.append(line.strip())
    return ls

print(read_file("63581-0.txt"))