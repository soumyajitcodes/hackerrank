import numpy as np

if __name__ == "__main__":
    p = np.array(input().split(), np.double)
    x = float(input())
    print(np.polyval(p, x))
