import cmath

if __name__ == "__main__":
    complex_number = complex(input())

    r, p = cmath.polar(complex_number)
    print(r)
    print(p)