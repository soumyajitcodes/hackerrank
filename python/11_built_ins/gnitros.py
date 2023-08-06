if __name__ == "__main__":
    s = input()
    a = []
    for i in range(0, len(s)):
        a.append(s[i])
    a.sort()
    lower = []
    upper = []
    oddDigits = ['1', '3', '5', '7', '9']
    evenDigits = ['0', '2', '4', '6', '8']
    od = []
    ev = []
    for i in range(0, len(a)):
        if a[i] >= 'A' and a[i] <= 'Z':
            upper.append(a[i])
        elif a[i] >= 'a' and a[i] <= 'z':
            lower.append(a[i])
        elif a[i] in oddDigits:
            od.append(a[i])
        elif a[i] in evenDigits:
            ev.append(a[i])

    print(''.join(lower) + ''.join(upper) + ''.join(od) + ''.join(ev))
