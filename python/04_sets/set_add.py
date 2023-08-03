if __name__ == "__main__":
    N = int(input())

    country_set = set()

    for _ in range(N):
        country = input()

        if country not in country_set:
            country_set.add(country)

    print(len(country_set))
