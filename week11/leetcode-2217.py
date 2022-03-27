# https://leetcode.com/contest/weekly-contest-286/problems/find-palindrome-with-fixed-length/

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ans = []
        oneIfEven = intLength % 2
        oneIfOdd = intLength % 2 > 0
        lBase = 10**(intLength//2-1+oneIfEven)
        for q in queries:
            lres = str(lBase-1+q)
            rres = lres[:len(lres)-oneIfOdd:][::-1]
            res = lres + rres
            print(f"lres:{lres}")
            print(f"rres:{rres}")
            print(res)
            if len(res) == intLength:
                res = int(res)
            else:
                res = -1
            ans.append(res)

        return ans
