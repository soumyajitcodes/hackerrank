from itertools import groupby

if __name__ == "__main__":
    S = input()

    for element, value in groupby(S):
        print(tuple([len(list(value)), int(element)]), end=" ")
