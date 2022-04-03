# PROBLEM_LINK
"""
Template reference: Emma, https://stackoverflow.com/a/62614733/13109740
"""

from typing import List
import collections
import itertools
import functools
import string
import random
import bisect
import re
import operator
import heapq
import queue

from math import *
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
    def foo(self, p1, p2):
        print(p1, p2)


print(Solution().foo(721, 831))