# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    n = int(input())
    for t in range(n):
        credit = input().strip()
        credit_removed_hiphen = credit.replace('-', '')
        valid = True

        length_16 = bool(re.match(r'^[4-6]\d{15}$', credit))
        length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', credit))
        consecutive = bool(re.findall(r'(?=(\d)\1\1\1)', credit_removed_hiphen))

        if length_16 or length_19:
            if consecutive:
                valid = False

        else:
            valid = False

        if valid:
            print('Valid')

        else:
            print('Invalid')
