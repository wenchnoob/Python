"""A function that determines whether two strings are anagrams or not"""


def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False

    string1 = list(string1)
    string2 = list(string2)
    string1.sort()
    string2.sort()

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    return True


print(is_anagram('mom', 'mom'))
print(is_anagram('mom', 'dad'))
print(is_anagram('listen', 'silent'))
