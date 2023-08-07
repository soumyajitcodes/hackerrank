if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        A = int(input())
        set_A = set(map(int, input().split()[:A]))
        B = int(input())
        set_B = set(map(int, input().split()[:B]))

        print(set_A.issubset(set_B))
