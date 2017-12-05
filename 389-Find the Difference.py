def findTheDifference(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count_s = {}
        count_t = {}
        
        for i in s:
            if count_s.get(i) == None:
            	count_s[i] = 1
            else:
            	count_s[i] += 1

        for i in t:
            if count_t.get(i) == None:
            	count_t[i] = 1
            else:
            	count_t[i] += 1

        for key in count_t:
        	if count_s.get(key) == None:
        		return key
        	elif count_t[key] != count_s[key]:
        		return key


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"

    results = findTheDifference(s, t)
    print results