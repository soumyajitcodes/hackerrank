import re

if __name__ == "__main__":
    pattern = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'

    for _ in range(int(input())):
        name, email = input().split(' ')

        if re.match(pattern, email):
            print(name, email)
