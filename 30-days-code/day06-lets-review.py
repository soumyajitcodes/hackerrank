if __name__ == "__main__":
    query = int(input())

    for _ in range(query):
        string = input()

        odd_charList = []
        even_charList = []

        for i in range(len(string)):
            if i % 2 == 0:
                even_charList.append(string[i])
            else:
                odd_charList.append(string[i])

        print(f"{''.join(even_charList)} {''.join(odd_charList)}")
