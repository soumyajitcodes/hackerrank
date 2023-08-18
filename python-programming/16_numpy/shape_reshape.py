import numpy


def arrays(int_array):
    changed_array = numpy.array(int_array)
    return numpy.reshape(changed_array, (3, 3))


if __name__ == "__main__":
    int_array = list(map(int, input().split()))
    result = arrays(int_array)
    print(result)
