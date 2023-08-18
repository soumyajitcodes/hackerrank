def maximumGold(x, z, arr, k):
    gold_count = 0

    while k:

        if gold_count != min(arr):
            gold_count += x

        elif gold_count in arr:
            element = arr.index(gold_count)
            x = x+z

            gold_count = gold_count-arr[element] +x
            arr.remove(gold_count)

        elif gold_count not in arr:
            for gold in arr:
                element = arr.index(gold_count)
                x = x + z

                gold_count = gold_count - arr[element] + x
                arr.remove(gold_count)

        k -= 1


    return gold_count


if __name__ == "__main__":
    # earn_gold_unit_per_day = int(input())  # x
    # extract_gold_per_day_machine = int(input())  # z
    # machine_count = int(input())  # n
    # machine_array = list(map(int, input().split()[:machine_count]))
    # days_count = int(input())  # k

    # result = maximumGoldold(earn_gold_unit_per_day, extract_gold_per_day_machine, machine_array, days_count)

    x = 1
    z = 2
    arr = list()
    arr.append(3)
    arr.append(2)
    arr.append(4)
    k = 5
    result = maximumGold(x, z, arr, k)

    print(result)
