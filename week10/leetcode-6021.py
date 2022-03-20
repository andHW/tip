# https://leetcode.com/contest/biweekly-contest-74/problems/maximize-number-of-subsequences-in-a-string/
"""
Template reference: Emma, https://stackoverflow.com/a/62614733/13109740

Thoughts:
aba
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
    def subCount(self, text, pat):
        a, b = len(text), len(pat)
        luTable = [0] * b

        for i in range(a):
            prev = 1
            for j in range(b):
                cur = luTable[j]
                if text[i] == pat[j]:
                    luTable[j] += prev
                prev = cur
        return luTable[-1]

    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        return(self.subCount(text, pattern))


print(Solution().maximumSubsequenceCount("aabb", "ab"))
print(Solution().maximumSubsequenceCount("aaabb", "ab"))
print(Solution().maximumSubsequenceCount("aaaabb", "ab"))
print(Solution().maximumSubsequenceCount("aaabbb", "ab"))
