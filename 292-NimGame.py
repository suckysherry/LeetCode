def canWinNim(n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0

if __name__ == '__main__':
    num = 4
    results = canWinNim(num)
    print results