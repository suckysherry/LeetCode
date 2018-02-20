import re
def calPoints(ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        nums = []
        temp = []
        total = 0
        for i in range(len(ops)):
            if re.findall(r"\d+",ops[i]):
                total += int(ops[i])
                nums.append(ops[i])
                print 'add', total, nums
            if ops[i] == 'C':
                total -= int(nums[i-1])
                nums.append(None)
                print 'c', total, nums
            if ops[i] == 'D':
                if nums[i-1]!=None:
                    flag = nums[i-1]
                for j in range(len(nums)):
                    if nums[j] == None:
                        flag = nums[j-2]
                total += (int(flag))*2
                nums.append(int(flag)*2)
                print 'd', total, nums
            if ops[i] == '+':
                temp = nums[::-1]
                print 'temp', temp
                if temp[0] != None and temp[1]!=None:
                    flag1 = temp[0]
                    flag2 = temp[1]
                else:
                    for j in range(len(temp)):
                        if temp[j] == None:
                            flag1 = temp[j-1]
                            flag2 = temp[j-2]
                total += (int(flag1))+(int(flag2))
                nums.append(int(flag1)+int(flag2))
                print 'flag1', flag1, 'fla2', flag2
                print '+', total, nums
        return total

if __name__ == '__main__':
    nums1 = ["5","2","C","D","+"]
    nums2 = ["5","-2","4","C","D","9","+","+"]
    nums3 = ["1","D","D","D"]
    nums4 = ["-60","D","-36","30","13","C","C","-33","53","79"]
    results = calPoints(nums4)
    print results