import re

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        try:
            re.compile(input())
            Output = True
        except re.error:
            Output = False

        print(Output)
