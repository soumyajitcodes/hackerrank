def minion_game(string):
    # your code goes here
    vowels = set('AEIOU')
    Stuart_Score = Kevin_Score = 0

    for i, s in enumerate(string):
        if s in vowels:
            Kevin_Score += len(string) - i
        else:
            Stuart_Score += len(string) - i

    if Stuart_Score > Kevin_Score:
        print('Stuart', Stuart_Score)
    elif Stuart_Score < Kevin_Score:
        print('Kevin', Kevin_Score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
