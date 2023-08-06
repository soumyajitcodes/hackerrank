if __name__ == "__main__":
    N = int(input())

    numbers = input().split()[:N]

    print(all([i > 0 for i in map(int, numbers)]) and any([i == i[::-1] for i in numbers]))
