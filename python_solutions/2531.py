class Solution:
    def is_eq(self,freq1,freq2):
        dis1 = 0
        dis2 = 0
        for i in range(26):
            char = chr(i+ord('a'))
            if freq1[char] > 0:
                dis1 += 1
            if freq2[char] > 0:
                dis2 += 1
        return dis1 == dis2
            
    def update_count(self,freq1,freq2,char1,char2):
        freq1[char1] -= 1
        freq2[char2] -= 1
        freq1[char2] += 1
        freq2[char1] += 1

    def isItPossible(self, word1: str, word2: str) -> bool:
        # Solution Overview
        # first count the distinct character in both strings
        # for each pair for characters in [a,z] find that swappnig these two make the string equal or not
        from collections import defaultdict
        freq1 = defaultdict(lambda : 0)
        freq2 = defaultdict(lambda : 0)
        for char in word1:
            freq1[char] += 1
        for char in word2:
            freq2[char] += 1
        for c1 in range(ord('a'),ord('z')+1):
            for c2 in range(ord('a'),ord('z')+1):
                char1 = chr(c1)
                char2 = chr(c2)
                if freq1[char1] > 0 and freq2[char2] > 0:
                    self.update_count(freq1,freq2,char1,char2)
                    if self.is_eq(freq1,freq2):
                        return True
                    self.update_count(freq1,freq2,char2,char1)
        return False
                    
        
