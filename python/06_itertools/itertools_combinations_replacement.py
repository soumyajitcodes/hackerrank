from itertools import combinations_with_replacement

if __name__ == "__main__":
    s, k = input().split()

    for element in combinations_with_replacement(sorted(s), int(k)):
        print(''.join(element))
