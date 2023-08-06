from collections import namedtuple

if __name__ == "__main__":
    N = int(input())

    students_tuple = namedtuple('Student', input().split())

    print(sum(float(students_tuple(*input().split()).MARKS) for _ in range(N)) / N)
