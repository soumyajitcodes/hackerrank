import re

if __name__ == "__main__":
    lines_count = int(input())

    for _ in range(lines_count):
        string = input()

        print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', string))
