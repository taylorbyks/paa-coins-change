import time


def reverseTimSort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
    return array


def getBiggerValue(array):
    biggerValue = 0
    for item in array:
        if item > biggerValue:
            biggerValue = item
    return biggerValue


def convertValueToCents(value):
    return int(float(value) * 100)


def openFile(filename):
    with open(filename, 'r') as f:
        value = convertValueToCents(f.readline())
        coins = []
        for line in f:
            coins = coins + line.split()
        coins = [int(coin) for coin in coins]

    return value, coins


def countCoins(coins):
    count = 0
    for coin in coins:
        count += coin * coins[coin]
    return count


def validate(coins, change, value):
    return change == countCoins(coins) and change >= value


def getTime(func, filename):
    value, coins = openFile(filename)
    start = time.time()
    change, changeCoins = func(value, coins)
    end = time.time()
    print("Value: ", value)
    print("Change: ", change)
    print("Coins: ", changeCoins)
    print("Is valid: ", validate(changeCoins, change, value))

    print("Tempo de execucao: ", end - start)
