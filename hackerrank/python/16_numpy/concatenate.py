import numpy

if __name__ == "__main__":
    N, M, P = map(int, input().split())

    arrayN = list()
    arrayM = list()

    for _ in range(N):
        n_row = list(map(int, input().split()))
        arrayN.append(n_row)

    for _ in range(M):
        m_row = list(map(int, input().split()))
        arrayM.append(m_row)

    arrayN = numpy.array(arrayN)
    arrayM = numpy.array(arrayM)

    print(numpy.concatenate((arrayN, arrayM), axis=0))
