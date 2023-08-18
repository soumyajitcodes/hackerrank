import datetime

if __name__ == "__main__":
    n = int(input())
    while n:
        dt1 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        dt2 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        print(abs(int(((dt2 - dt1).total_seconds()))))
        n -= 1
