import re

if __name__ == "__main__":
    regex_pattern = r'[789]\d{9}$'

    testcase_count = int(input())

    for _ in range(testcase_count):
        string = input()
        print('YES' if re.match(regex_pattern, string) else 'NO')
