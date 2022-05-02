# https://leetcode.com/contest/biweekly-contest-77/problems/count-prefixes-of-a-given-string/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for w in words:
            if s.startswith(w):
                ans+=1
        return ans