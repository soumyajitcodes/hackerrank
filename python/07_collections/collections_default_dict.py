from collections import defaultdict

if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))
    A = defaultdict(list)

    for i in range(n):
        l = input()
        A[l].append(i + 1)

    for i in range(m):
        l = input()
        if len(A[l]) == 0:
            print(-1)
        else:
            print(*A[l])
