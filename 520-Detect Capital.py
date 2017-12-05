def detectCapitalUse(word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower():
            return True
        if word.isupper():
            return True

        flag = 0
        if word[0].isupper:
            for i in word[1:]:
                if i.isupper():
                    return False
                else:
                    flag = 1
            if flag == 1:
                return True

if __name__ == '__main__':
    results = detectCapitalUse('USA')
    print results
