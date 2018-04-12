def change_prob(coin_value_list, change):
    min_coin = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + change_prob(coin_value_list, change-i)
            if num_coins < min_coin:
                min_coin = num_coins

        return min_coin

print(change_prob([1,5,10,25], 63))
