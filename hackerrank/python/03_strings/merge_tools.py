def merge_the_tools(string, k):
    # your code goes here
    """merge_Tools"""
    for i in range(int(len(string) / k)):
        l = []
        for j in range(k):
            ch = string[i * k + j]
            if ch not in l:
                l += [ch]
        a = ''.join(l)
        print(a)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
