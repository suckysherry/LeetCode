import math
def constructRectangle(area):
        """
        :type area: int
        :rtype: List[int]
        """
        rlist = [0,0]
        w = 0
        l = 0
        carry = 0
        smallest = 100000
        a = int(math.sqrt(area))
        if pow(a,2) == area:
        	return [a, a]
        else:
        	for num in range(1,area):
        		if area%num == 0:
        			w = num
        			l = area/num
        			carry = w-l
        			if abs(carry)<smallest:
        				smallest = abs(carry)
        				rlist = [l,w]
        				print 'rlist', rlist
        return rlist



if __name__ == '__main__':
    m = 2
    results = constructRectangle(m)
    print results