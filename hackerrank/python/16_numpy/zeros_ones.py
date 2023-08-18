import numpy

if __name__ == "__main__":
    N = list(map(int, input().split()))
    ZEROS = numpy.zeros((N), int)
    ONES = numpy.ones((N), int)
    print(ZEROS, ONES, sep="\n")
