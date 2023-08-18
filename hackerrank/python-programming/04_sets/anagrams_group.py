def count_anagrams(string_list):
    anagram_dict = {}

    for word in string_list:
        anagram_word = ''.join(sorted(word))
        if anagram_word not in anagram_dict:
            anagram_dict[anagram_word] = [word]
        else:
            anagram_dict[anagram_word] += [word]

    return len(anagram_dict)


if __name__ == "__main__":
    n = int(input())
    string_list = input().split()

    print(count_anagrams(string_list))
