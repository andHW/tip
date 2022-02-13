# https://leetcode.com/contest/weekly-contest-280/problems/count-operations-to-obtain-zero/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:        
        if num1<num2:
            num1, num2 = num2, num1
        # num1 >= num2 at this point
        
        operations = 0
        while num1>0 and num2 >0:
            print(num1,num2)
            num1-=num2
            if num1<num2:
                num1, num2 = num2, num1
            operations+=1
            
        return operations