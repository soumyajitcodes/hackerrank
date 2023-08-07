cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        temp = fib[-1] + fib[-2]
        fib.append(temp)
    return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
