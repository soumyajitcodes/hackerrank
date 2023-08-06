if __name__ == "__main__":
    k = int(input())
    rooms = (int(x) for x in input().split())
    seen = {}
    for i in rooms:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1

    for key, val in seen.items():
        if val != k:
            print(key)
