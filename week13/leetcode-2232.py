# https://leetcode.com/contest/weekly-contest-288/problems/minimize-result-by-adding-parentheses-to-expression/
# Brute force

class Solution:
    def minimizeResult(self, expression: str) -> str:
        exp = expression
        best = '('+exp+')'
        bVal = eval(best)
        plus = exp.index('+')
        for i in range(plus):
            for j in range(plus+1,len(exp)):
                newExp = list(exp)
                newExp.insert(i,"(")
                newExp.insert(i+j+1,")")
                
                sexp = "".join(newExp)
                
                if sexp.index("(")>0:
                    sexp = sexp.replace("(", "*(")
                
                if sexp.index(")")<len(sexp)-1:
                    sexp = sexp.replace(")", ")*")
                
                print(sexp)
                try:
                    newVal = eval(sexp)
                    if newVal < bVal:
                        bVal = newVal
                        best = sexp
                except:
                    continue
        
        return best.replace("*","")