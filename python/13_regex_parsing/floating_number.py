import re

if __name__ == "__main__":
    n = int(input())
    pattern = re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
    for _ in range(n):
        print(pattern.match(input()) is not None)