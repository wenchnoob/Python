"""Script to analyze a plaintext file"""


def analyze_plaintext(name):
    total_chars = 0
    total_words = 0
    avg_word_len = 0

    char_counts = dict()

    # Opened with context manager...benefit is auto closed.
    with open(name, 'r') as file:
        for line in file:
            line = line.strip()
            total_chars += len(line)
            total_words += 1

            for i in range(len(line)):
                if line[i] not in char_counts:
                    char_counts[line[i]] = 1
                else:
                    char_counts[line[i]] = char_counts.get(line[i]) + 1
    avg_word_len = total_chars / total_words
    return total_chars, total_words, avg_word_len, char_counts


def main():
    name = 'words.txt'
    info = analyze_plaintext(name)

    total_chars = info[0]
    total_words = info[1]
    avg_word_len = info[2]
    char_count_dict = info[3]

    head = "The {:s} file has been analyzed and below there will be some analytics listed.".format(name)
    summary = "The file has {:d} words and {:d} characters. The words in the file have an average length of {:.3f}" \
        .format(total_words, total_chars, avg_word_len)

    print(head + "\n\n" + summary + "\n\n\n" + "This is the percent make up of each character in the file: ")

    percent_makeup = ""
    for key in char_count_dict:
        percent = (char_count_dict[key] / total_chars) * 100
        percent_makeup += "{:3s}| {:2.2f}%\n".format(key, percent)
    print(percent_makeup)


main()
