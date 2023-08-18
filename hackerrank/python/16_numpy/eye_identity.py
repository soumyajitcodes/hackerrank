import numpy

numpy.set_printoptions(legacy="1.13")
if __name__ == "__main__":
    N, M = map(int, input().split())

    print(numpy.eye(N, M))
