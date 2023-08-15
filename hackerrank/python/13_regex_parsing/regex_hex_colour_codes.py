import re

if __name__ == "__main__":
    for _ in range(int(input())):
        matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
        if matches:
            print(*matches, sep='\n')
