def isToeplitzMatrix(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        1,2,3,4
        5,1,2,3
        9,5,1,2

        11,74,0.93
        40,11,74,7

        53,64,90,98,34
        91,53,64,90,98
        17,91,53,64,0

        row = len(matrix)
        col = len(matrix[0])
        results = []

        for i in range(row):
        	for j in range(col):
        		print '[', i, ',', j, ']'
    			if i+1 < row and j + 1 < col:
    				print matrix[i][j], matrix[i+1][j+1]
        			if matrix[i][j]!= matrix[i+1][j+1]:
        				print 'not equal'
        				results.append(1)
        			else:
        				print 'equal'
        				results.append(0)
        			print results
        total = sum(results)
        if total == 0:
        	return True
        else:
        	return False


if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    matrix1 = [[11,74,0,93],[40,11,74,7]]
    matrix2 = [[53,64,90,98,34],[91,53,64,90,98],[17,91,53,64,0]]
    result = isToeplitzMatrix(matrix2)
    print result