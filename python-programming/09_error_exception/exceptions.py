if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except ZeroDivisionError as zde:
            print("Error Code:", zde)
        except ValueError as ve:
            print("Error Code:", ve)
