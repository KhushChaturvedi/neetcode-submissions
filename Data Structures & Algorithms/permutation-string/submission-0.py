class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counts1 = {}
        counts2 = {}

        for char in s1:
            counts1[char] = counts1.get(char,0)+1
        for char in s2[0 : len(s1)]:
            counts2[char] = counts2.get(char,0)+1

        if counts1 == counts2:
            return True
        else:
            for i in range(len(s1) , len(s2)):
                counts2[s2[i]] = counts2.get(s2[i],0)+1

                old_char = s2[i - len(s1)]
                counts2[old_char] -= 1

                if counts2[old_char] == 0:
                    del counts2[old_char]

                if counts1 == counts2:
                    return True
            return False