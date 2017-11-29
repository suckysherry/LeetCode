def matrixReshape(nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c > len(nums)*len(nums[0]):
            return nums

        row = []
        for i in nums:
            row.extend(i)
        print row

        new_nums = []
        flag = 0
        for i in range(r):
            temp = []
            for j in range(flag, flag + c):
                temp.append(row[j])
            new_nums.append(temp)
            flag += c

        return new_nums

if __name__ == '__main__':
    List = [[1,2],[3,4], [5,6]]
    r = 1
    c = 4
    results = matrixReshape(List, 2, 3)
    print results
