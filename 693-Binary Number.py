def hasAlternatingBits(n):
        """
        :type n: int
        :rtype: bool
        """
        intbin = bin(n)
        strbin = str(intbin)[2:]

        if len(strbin) == 1:
            return True

        flag = True
        for i in range(len(strbin)-1):
            if strbin[i] == strbin[i+1]:
                flag = False
                break
        return flag
if __name__ == '__main__':
    results = hasAlternatingBits(4)
    print results
