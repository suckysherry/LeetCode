def getSum(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0X7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        
        while b != 0:
            xor = (a^b) & mask
            bit = ((a&b)<<1) & mask
            a = xor
            b = bit
        return a if a<=MAX else ~(a^mask)
        

if __name__ == '__main__':
    num1 = -1
    num2 = 1

    results = getSum(num1, num2)
    print results