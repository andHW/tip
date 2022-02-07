# https://leetcode.com/contest/weekly-contest-279/problems/smallest-value-of-the-rearranged-number/
class Solution:
    def smallestNumber(self, num: int) -> int:
        negative = False
        if num < 0:
            negative = True
            num = abs(num)

        ds = [int(d) for d in str(num)]

        ans = ""
        if negative:
            ds.sort(reverse=True)
            ans = "-"
        else:
            ds.sort()
            smallestNonZero = ds[-1]
            for d in ds:
                if d < smallestNonZero and d > 0:
                    smallestNonZero = d
            ans = str(smallestNonZero)

            ds.remove(smallestNonZero)

        ans += "".join([str(d) for d in ds])
        print(ans)
        return ans
