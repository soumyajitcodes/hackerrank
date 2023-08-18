from itertools import permutations

if __name__ == "__main__":
    s, k = input().split()

    for element in sorted(permutations(s, int(k))):
        print(''.join(element))
