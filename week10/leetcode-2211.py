class Solution:
    def countCollisions(self, directions: str) -> int:
        res = 0
        ds = directions
        res+=ds.count("RL")*2
        ds = ds.replace("RL","SS")
        
        firstS = ds.find("S")
        lastS = ds.rfind("S")
        
        if firstS!=-1 or lastS!=-1:
            res+=ds[:firstS].count("R")
            print(res)
            res+=ds[lastS:].count("L")
            print(res)
            res+=ds[firstS:lastS].count("R")
            res+=ds[firstS:lastS].count("L")
            print(res)
        
        # print(ds)
        # while "RS" in ds or "SL" in ds:
        #     res+=ds.count("RS")
        #     ds = ds.replace("RS","SS")
        #     res+=ds.count("SL")
        #     ds = ds.replace("SL","SS")
        # print(ds)
        
        return res