# Coin Change - Dynamically


def rec_coin_dynam(target, coins, known_results):
    '''
    INPUT: This function takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter should be started with [0] * (target+1)

    OUTPUT: Minimum number of coins needed to make the target.
    '''
    # Default output to target
    min_coins = target

    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1

    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]

    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

                # Reset the known result
                known_results[target] = min_coins

    return min_coins


target = 85
coins = [1, 10, 15, 25]
known_results = [0]*(target+1)

result = rec_coin_dynam(target, coins, known_results)

print(result)
