if __name__ == "__main__":
    M = int(input())
    set_m = set(map(int, input().split()))

    N = int(input())
    set_n = set(map(int, input().split()))

    symmetric_difference = set_m.symmetric_difference(set_n)

    for element in sorted(symmetric_difference):
        print(element)
