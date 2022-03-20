#https://leetcode.com/contest/weekly-contest-285/problems/maximum-points-in-an-archery-competition/

class Solution:
    @cache
    def ks(self, shootableAs, target, curScore, sAs, output) -> int:
        if shootableAs<1 or target<0:
            return (curScore,shootableAs,output)
        
        notShooting = self.ks(shootableAs, target-1, curScore, sAs, output)
        
        if sAs[target] > shootableAs:
            return notShooting
        
        newOutput = list(output[:])
        newOutput[target] = sAs[target]
        newOutput = tuple(newOutput)
        shooting = self.ks(shootableAs-sAs[target], target-1, curScore+target, sAs,newOutput)
        
        return max(shooting,notShooting)
            
        
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        # aliceArrows = weight
        # score = profit
        scoringArrows = [a+1 for a in aliceArrows]
        print(scoringArrows)
        output = [0]*12
        ans,shootables,op = self.ks(numArrows, 11, 0, tuple(scoringArrows), tuple(output))
        op = list(op)
        op[0] = shootables
        return op