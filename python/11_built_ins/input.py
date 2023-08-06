if __name__ == "__main__":
    x, k = map(int, input().split())
    P = input()
    if eval(P) == k:
        print("True")
    else:
        print("False")
