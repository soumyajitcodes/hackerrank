if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    winner_score = max(arr)

    for i in range(n):
        if winner_score in arr:
            arr.remove(winner_score)

    print(max(arr))
