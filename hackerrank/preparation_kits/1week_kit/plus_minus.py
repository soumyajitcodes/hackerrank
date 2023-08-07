def plusMinus(arr):
    zero_count = 0
    positive_count = 0
    negative_count = 0
    array_len = len(arr)

    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    # Proportion of Positive Values
    print("{:.6f}".format(round(positive_count / array_len, 6)))
    # Proportion of Negative Values
    print("{:.6f}".format(round(negative_count / array_len, 6)))
    # Proportion of Zero Values
    print("{:.6f}".format(round(zero_count / array_len, 6)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
