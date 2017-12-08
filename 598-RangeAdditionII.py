def maxCount(m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # r = []
        # c = []
        # temp = []
        # nums = [[0 for i in range(n)] for i in range(m)]#m*n Array
        # for op in ops:
        # 	r = op[0]
        # 	c = op[1]
        # 	for i in range(r):
        # 		for j in range(c):
        # 			nums[i][j]+=1
        # 	print nums
        # for i in nums:
        # 	temp.extend(i)
        # MAX = max(temp)
        # count = 0
        # for i in temp:
        # 	if i == MAX:
        # 		count+=1
        # return count
        return m*n if not ops else min(op[0] for op in ops)*min(op[1] for op in ops)





if __name__ == '__main__':
    m = 3
    n = 3
    ops = [[2,2],[3,3]]
    results = maxCount(m, n, ops)
    print results