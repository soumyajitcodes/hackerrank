import numpy

if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    arr1 = numpy.array([input().split() for _ in range(N)], int)
    arr2 = numpy.array([input().split() for _ in range(N)], int)

    print(numpy.add(arr1, arr2))
    print(numpy.subtract(arr1, arr2))
    print(numpy.multiply(arr1, arr2))
    print(numpy.floor_divide(arr1, arr2))
    print(numpy.mod(arr1, arr2))
    print(numpy.power(arr1, arr2))
