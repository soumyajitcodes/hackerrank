if __name__ == "__main__":
    A = int(input())
    set_A = set(map(int, input().split()[:A]))

    N = int(input())

    for _ in range(N):
        set_operation_size = input().split()
        set_B = set(map(int, input().split()[:int(set_operation_size[1])]))

        if set_operation_size[0] == 'update':
            set_A.update(set_B)
        elif set_operation_size[0] == 'intersection_update':
            set_A.intersection_update(set_B)
        elif set_operation_size[0] == 'difference_update':
            set_A.difference_update(set_B)
        elif set_operation_size[0] == 'symmetric_difference_update':
            set_A.symmetric_difference_update(set_B)

    print(sum(set_A))
