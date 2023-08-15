import re

if __name__ == "__main__":
    S = input()
    k = input()

    pattern = re.compile(k)

    match = pattern.search(S)

    if not match:
        print("(-1, -1)")

    while match:
        print('({0}, {1})'.format(match.start(), match.end() - 1))
        match = pattern.search(S, match.start() + 1)
