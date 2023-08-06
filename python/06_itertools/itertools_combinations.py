from itertools import combinations

if __name__ == "__main__":
    s, i = input().split()
    s = list(s)
    i = int(i)
    s.sort()
    for j in range(1, i + 1):
        for k in list(combinations(s, j)):
            print(''.join(k))
