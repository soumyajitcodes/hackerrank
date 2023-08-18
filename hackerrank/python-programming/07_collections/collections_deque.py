from collections import deque

if __name__ == "__main__":
    N = int(input())
    d = deque()

    for _ in range(N):
        command = input().split()

        if command[0] == "append":
            d.append(int(command[1]))
        elif command[0] == "pop":
            d.pop()
        elif command[0] == "popleft":
            d.popleft()
        else:
            d.appendleft(int(command[1]))

    for elements in d:
        print(elements, end=" ")
