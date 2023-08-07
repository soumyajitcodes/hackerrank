def happiness_count(num_list, set_a, set_b):
    happiness = 0

    for num in num_list:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
        else:
            happiness += 0

    return happiness


if __name__ == "__main__":
    n, m = map(int, input().split())

    num_list = list(map(int, input().split()))

    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    print(happiness_count(num_list, set_a, set_b))
