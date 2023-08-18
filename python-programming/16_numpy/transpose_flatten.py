import numpy

if __name__ == "__main__":
    N, M = map(int, input().split())

    integer_array = list()

    for _ in range(N):
        row = list(map(int, input().split()))

        integer_array.append(row)

    converted_array = numpy.array(integer_array)

    print(numpy.transpose(converted_array))
    print(converted_array.flatten())
