import numpy

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    arr = numpy.array([input().split() for _ in range(N)], float)
    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(round(numpy.std(arr), 11))
