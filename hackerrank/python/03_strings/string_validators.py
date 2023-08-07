if __name__ == '__main__':
    s = input()

    # alphanumeric check
    print(any(x.isalnum() for x in s))
    # alphabetic characters
    print(any(x.isalpha() for x in s))
    # digits check
    print(any(x.isdigit() for x in s))
    # lower case check
    print(any(x.islower() for x in s))
    # upper case check
    print(any(x.isupper() for x in s))
