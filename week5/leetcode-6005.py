from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums)<2: return 0
        evens = []
        odds = []
        
        isEven = True
        for n in nums:
            if isEven:
                evens+=[n]
            else:
                odds+=[n]
            isEven = not isEven
        print(evens)
        print(odds)
        
        eCounter = Counter(evens).most_common(2)
        oCounter = Counter(odds).most_common(2)
        
        eMax1Num, eMax1Count = eCounter[0]
        oMax1Num, oMax1Count = oCounter[0]
        if eMax1Num != oMax1Num:
            return len(evens)-eMax1Count + len(odds)-oMax1Count
        if len(eCounter)<2 and len(oCounter)<2:
            return len(nums) //2
        eMax2Count = 0
        oMax2Count = 0
        if len(eCounter)>1:
            _, eMax2Count = eCounter[1]
        if len(oCounter)>1:
            _, oMax2Count = oCounter[1]
        
        a = len(evens) + len(odds) - eMax1Count - oMax2Count
        b = len(evens) + len(odds) - eMax2Count - oMax1Count
        
        return min(a,b)
            