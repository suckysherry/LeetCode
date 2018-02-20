def letterCasePermutation(S):
        """
        :type S: str
        :rtype: List[str]
        """

        result = []
        results = [S]
        leng = len(S)

        for i in range(leng):
        	for item in results:
        		if item[i].isalpha() == True:
        			result = item[0:i]+item[i].upper()+item[i+1:leng]
        			if result not in results:
        				results.append(result)
        			result = item[0:i]+item[i].lower()+item[i+1:leng]
        			if result not in results:
        				results.append(result)
        return results
        


if __name__ == '__main__':
    S = "a1b2"
    S1 = "3z4"
    S2 = 'FKqeaCFIESzo'
    result = letterCasePermutation(S1)
    print result