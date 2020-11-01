import AnalysisHelper


def count_words(words):
    return len(words)


def count_chars(words):
    count = 0
    for word in words:
        count += len(word)
    return count


def main():
    name = "58175-8.txt"
    words = AnalysisHelper.parse_file(name)
    word_count = count_words(words)
    char_count = count_chars(words)
    average_word_length = char_count / word_count

    print("Stats for analyzed file: \n\nName: {:>22s} \nWord Count: {:>16.2f} \nCharacter count: {:>11.2f} \n" \
          "Average word length: {:>7.2f} \n".format(name, word_count, char_count, average_word_length))

    char_count_dict = AnalysisHelper.count_chars(words)
    char_count_list = sorted(char_count_dict.items(), key=lambda x: x[1], reverse=True)

    print("The percent makeup of each letter in the file is as follows: \n")
    percent_makeup = ""
    for key in char_count_list:
        percent = (key[1] / char_count) * 100
        percent_makeup += "{:3s}| {:2.2f}%\n".format(key[0], percent)
    print(percent_makeup)


main()
