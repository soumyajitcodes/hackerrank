if __name__ == "__main__":
    english_newspaper_count = int(input())
    english_newspaper_set = set(map(int, input().split()[:english_newspaper_count]))

    french_newspaper_count = int(input())
    french_newspaper_set = set(map(int, input().split()[:french_newspaper_count]))

    print(len(english_newspaper_set.intersection(french_newspaper_set)))
