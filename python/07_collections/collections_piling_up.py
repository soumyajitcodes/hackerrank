from collections import deque

if __name__ == "__main__":
    d = deque()
    for _ in range(int(input())):
        _ = int(input())

        for x in input().split():
            d.append(int(x))

        last_pop = 2 ** 31
        while len(d) != 0:
            if last_pop >= d[0] >= d[-1]:
                last_pop = d.popleft()
            elif last_pop >= d[-1] >= d[0]:
                last_pop = d.pop()
            else:
                break

        print("Yes" if len(d) == 0 else "No")
        d.clear()
