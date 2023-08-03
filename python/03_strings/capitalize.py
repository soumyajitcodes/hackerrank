#!/bin/python3

import os


# Complete the solve function below.
def solve(s):
    names = s.split(' ')
    capitalized_names = [name.capitalize() for name in names]
    result = ' '.join(capitalized_names)
    return result


if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
