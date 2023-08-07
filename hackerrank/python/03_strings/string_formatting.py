def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])

    for num in range(1, number + 1):
        decimal = str(num)
        octal = (oct(num))[2:]
        hexadecimal = (hex(num))[2:].upper()
        binary = (bin(num))[2:]

        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
