import math
def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    stnum = str(num)
    if len(stnum) == 1:
        return num

    return int(num - 9*(math.floor((num-1)/9)))


if __name__ == '__main__':
    num = 38
    results = islandPerimeter(num)
    print results
