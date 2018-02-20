
def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    counts = []
    for item in J:
        count = 0
        for jtem in S:
            if item == jtem:
                count += 1
        counts.append(count)
        
    return sum(counts)

if __name__ == '__main__':
    J = 'aAA'
    S = "aAAbbbb"
    print J, S
    result = numJewelsInStones(J, S)
    print result