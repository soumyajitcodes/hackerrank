def count_substring(string, sub_string):
    sub_string_list = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]

    sub_string_count = 0

    for subString in sub_string_list:
        if subString == sub_string:
            sub_string_count += 1

    return sub_string_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
