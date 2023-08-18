import numpy

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    arr = numpy.array([input().split() for _ in range(N)], int)
    print(numpy.max(numpy.min(arr, axis=1)))
