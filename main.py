import utils


def greedy(value, coins):
    change = 0
    changeCoins = []

    while value > change and len(coins) > 0:
        coin = utils.getBiggerValue(coins)
        coins.remove(coin)
        changeCoins.append(coin)
        change += coin

    return change, changeCoins


utils.getTime(greedy, "./inputs/Troco5000.txt")
