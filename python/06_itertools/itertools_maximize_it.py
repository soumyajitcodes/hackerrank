if __name__ == "__main__":
    data = input().split()
    k = int(data[0])
    m = int(data[1])
    states = [0]
    for i in range(k):
        newstates = []
        data = input().split()
        for st in data[1:]:
            d = int(st)
            for s in states:
                newtot = (d * d + s) % m
                if not (newtot in newstates):
                    newstates.append(newtot)
        states = newstates
    print(max(states))