# Enter your code here. Read input from STDIN. Print output to STDOUT
def strnrepeat(string):
    string_array = string.split()

    final_string = []

    for word in string_array:
        num = 0
        string_list = []
        for char in word:
            if char.isdigit():
                num = num + int(char)
            else:
                string_list.append(char)

        string_without_digits = ''.join(string_list)

        if num > 0:
           final_string.append(string_without_digits * num)
        else:
            final_string.append(string_without_digits*1)

    return ' '.join(final_string)


if __name__ == '__main__':
    string = "Initialize a0n em2pt0y st3rin4g"

    print(strnrepeat(string))
