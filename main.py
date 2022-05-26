import utils
import sys
sys.setrecursionlimit(50000)


def getBiggerValue(array):
    biggerValue = 0
    for item in array:
        if item > biggerValue:
            biggerValue = item
    return biggerValue


def greedy(value, coins):
    change = 0
    changeCoins = {}

    while value > change and len(coins) > 0:
        coin = getBiggerValue(coins)
        while coin + change > value:
            if len(coins) == 1:
                break
            coins.remove(coin)
            coin = getBiggerValue(coins)
        coins.remove(coin)
        changeCoins[coin] = changeCoins.get(coin, 0) + 1
        change += coin

    return change, changeCoins


def greedySort(value, coins):
    sortCoins = utils.reverseTimSort(coins)
    sortCoins.reverse()
    change = 0
    changeCoins = {}

    while value > change and len(sortCoins) > 0:
        + 2
        i = 0
        coin = sortCoins[i]
        while coin + change > value:
            i += 1
            coin = sortCoins[i]
        sortCoins.remove(coin)
        changeCoins[coin] = changeCoins.get(coin, 0) + 1
        change += coin

    return change, changeCoins


def bruteForce(value, coins, changeCoins={}, change=0):
    if change >= value:
        return change, changeCoins

    for coin in coins:
        if coin + change <= value:
            changeCoins[coin] = changeCoins.get(coin, 0) + 1
            change += coin
            return bruteForce(value, coins, changeCoins, change)


utils.getTime(greedy, "./inputs/Troco10.txt")
utils.getTime(greedySort, "./inputs/Troco10.txt")
utils.getTime(bruteForce, "./inputs/Troco500.txt")
