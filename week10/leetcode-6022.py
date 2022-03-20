# https://leetcode.com/contest/biweekly-contest-74/problems/minimum-operations-to-halve-array-sum/
"""
Template reference: Emma, https://stackoverflow.com/a/62614733/13109740
"""

from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        csum = isum = sum(nums)
        ans = 0
        half = isum/2.0

        nums = [-n for n in nums]
        heapq.heapify(nums)
        print(nums)
        while csum > half:
            nmax = heapq.heappop(nums)
            nmax/=2.0
            csum+=nmax
            heapq.heappush(nums,nmax)
            ans += 1
            print(csum, half)
        return ans


print(Solution().halveArray([5, 19, 8, 1]))
print(Solution().halveArray([2, 2, 2, 2]))
print(Solution().halveArray([10000000, 6000000, 1, 1]))
print(Solution().halveArray([6,58,10,84,35,8,22,64,1,78,86,71,77]))
