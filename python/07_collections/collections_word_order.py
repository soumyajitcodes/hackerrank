from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())

    string_dict = OrderedDict()

    for _ in range(n):
        string = input()
        if string not in string_dict:
            string_dict[string] = 1
        else:
            string_dict[string] += 1

    print(len(string_dict))

    for k, v in string_dict.items():
        print(v, end=" ")