import utils


def greedy(value, coins):
    change = 0
    changeCoins = {}

    while value > change and len(coins) > 0:
        coin = utils.getBiggerValue(coins)
        while coin + change > value:
            if len(coins) == 1:
                break
            coins.remove(coin)
            coin = utils.getBiggerValue(coins)
        coins.remove(coin)
        changeCoins[coin] = changeCoins.get(coin, 0) + 1
        change += coin

    return change, changeCoins


def greedySort(value, coins):
    sortCoins = sorted(coins, reverse=True)
    change = 0
    changeCoins = {}

    while value > change and len(sortCoins) > 0:
        i = 0
        coin = sortCoins[i]
        while coin + change > value:
            i += 1
            coin = sortCoins[i]
        sortCoins.remove(coin)
        changeCoins[coin] = changeCoins.get(coin, 0) + 1
        change += coin

    return change, changeCoins


utils.getTime(greedy, "./inputs/Troco5000.txt")
utils.getTime(greedySort, "./inputs/Troco5000.txt")
