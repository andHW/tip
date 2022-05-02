class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        magic = defaultdict(list)
        for i, c in enumerate(cards):
            magic[c].append(i)
        print(magic)
        
        res = -1
        good = False
        for m in magic:
            if len(magic[m]) > 1:
                res = magic[m][1] - magic[m][0] + 1
                good = True
                break
        
        if not good:
            return -1
        
        for m in magic:
            if len(magic[m]) < 2:
                continue
            mm = magic[m]
            for a,b in zip(mm, mm[1:]):
                if b-a+1 < res:
                    res = b-a+1
                    if res == 2:
                        return 2
                
        return res