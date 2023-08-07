if __name__ == "__main__":
    N = int(input())
    num_tuple = tuple(map(int, input().split()[:N]))

    print(hash(num_tuple))
