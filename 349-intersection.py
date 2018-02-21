def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # long_len = len(nums1)
        # short_len = len(nums2)
        # result = []

        # if long_len < short_len:
        # 	long_len, short_len = short_len, long_len
        # 	short_list = nums1
        # 	long_list = nums2
        # else:
        # 	short_list = nums2
        # 	long_list = nums1

        # for i in range(short_len):
        # 	for j in range(long_len):
        # 		if short_list[i] == long_list[j]:
        # 			result.append(short_list[i])

        # result = list(set(result))
        # return result

        return list(set(nums2)&set(nums1))


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = intersection(nums1, nums2)
    print result