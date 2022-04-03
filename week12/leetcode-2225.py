# https://leetcode.com/contest/weekly-contest-287/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lostCounts = defaultdict(int)
        possibleWinners = set()
        for w,l in matches:
            possibleWinners.add(w)
            lostCounts[l]+=1
        
        answer1=[]
        answer2=[]
        
        for w in possibleWinners:
            if lostCounts[w] <1:
                answer1.append(w)
        for loser in lostCounts:
            if lostCounts[loser] ==1:
                answer2.append(loser)
        
        answer1.sort()
        answer2.sort()
        
        
        return [answer1, answer2]