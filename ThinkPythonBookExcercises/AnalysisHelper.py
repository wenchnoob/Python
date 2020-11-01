def read_file(name):
    ls = []
    with open(name, 'r') as file:
        for line in file:
            ls.append(line.strip())
    return ls


def clean_line(my_str):
    my_str = list(my_str)
    for i in range(len(my_str)):
        if not my_str[i].isalpha() and not my_str[i].isspace():
            my_str[i] = ''
    return ''.join(my_str)


def split_sentences(lines):
    words = []
    for x in lines:
        if not len(x) == 0:
            words = words + x.lower().split(" ")
    return words


def parse_file(name):
    lines = read_file(name)
    for i in range(len(lines)):
        lines[i] = clean_line(lines[i])
    return split_sentences(lines)


def count_chars(words):
    char_counts = dict()

    for word in words:
        for char in word:
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] = char_counts.get(char) + 1
    return char_counts
