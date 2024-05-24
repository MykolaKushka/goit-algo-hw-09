def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    return result

print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    # Ініціалізуємо масив для збереження мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  
    # Ініціалізуємо масив для відстеження використовуваних монет
    coin_used = [0] * (amount + 1)
    
    # Динамічне програмування для заповнення масиву dp
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin
    
    # Відновлення мінімальної кількості монет для заданої суми
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

print(find_min_coins(113))  # {1: 1, 2: 1, 10: 1, 50: 2}
