def timeConversion(s):
    # Write your code here
    str_ = s[-2:]
    if str_ == "AM" and s[0:2] == "12":
        s = s.replace("12", "00")
    elif str_ == "PM" and s[0:2] != "12":
        s = s.replace(s[0:2], str(int(s[0:2]) + 12))
    return s[0:-2]


if __name__ == "__main__":
    s = input()

    result = timeConversion(s)

    print(result)
