import numpy

numpy.set_printoptions(legacy="1.13")
if __name__ == "__main__":
    array = numpy.array(list(map(float, input().split())))

    print(numpy.floor(array))
    print(numpy.ceil(array))
    print(numpy.rint(array))
