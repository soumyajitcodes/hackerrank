if __name__ == "__main__":
    shoe_count = int(input())
    shoe_size_list = list(map(int, input().split()[:shoe_count]))

    customer_count = int(input())
    customer_shoe_size = []
    customer_shoe_price = []

    while customer_count:
        size, price = map(int, input().split())
        customer_shoe_size.append(size)
        customer_shoe_price.append(price)

        customer_count -=1

    money_earned = 0
    for i in range(len(customer_shoe_size)):
        if customer_shoe_size[i] in shoe_size_list:
            money_earned += customer_shoe_price[i]
            shoe_size_list.remove(customer_shoe_size[i])

    print(money_earned)