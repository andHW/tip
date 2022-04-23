class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = defaultdict(int)
        for t in tasks:
            counter[t]+=1
        
        magic = []
        for c in counter:
            magic.append(counter[c])
        magic.sort(reverse=True)
        print(magic)
        
        res = 0
        for m in magic:
            if m<2:
                return -1
            if m == 4:
                res += 2
                continue
            
            
            
            threes = m//3 - int(m%3==1)
            twos = (m-3*threes)//2
            print(f"{threes} {twos}")
            res += threes + twos
            
        return res