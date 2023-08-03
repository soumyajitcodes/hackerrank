if __name__ == '__main__':
    N = int(input())

    num_list = []

    for _ in range(N):
        command = input().split()

        if command[0] == 'insert':
            num_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(num_list)
        elif command[0] == 'remove':
            num_list.remove(int(command[1]))
        elif command[0] == 'append':
            num_list.append(int(command[1]))
        elif command[0] == 'sort':
            num_list.sort()
        elif command[0] == 'pop':
            num_list.pop()
        elif command[0] == 'reverse':
            num_list.reverse()
