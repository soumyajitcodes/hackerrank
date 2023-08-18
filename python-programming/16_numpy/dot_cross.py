import numpy

def read_matrix(n):
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    return numpy.array(l)

if __name__ == "__main__":
    n = int(input())
    a = read_matrix(n)
    b = read_matrix(n)
    print(numpy.matmul(a, b))