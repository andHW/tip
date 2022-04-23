class ATM:

    def __init__(self):
        self.count = [0]*5
        self.dems = [20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, bncount in enumerate(banknotesCount):
            self.count[i] += bncount
        print(f"DEPOSIT: {self.count}")

    def withdraw(self, amount: int) -> List[int]:
        res = [0]*5
        for itr in range(4, -1, -1):
            c = self.count[itr]
            v = self.dems[itr]
            if c<1: continue
            if amount<v: continue
            
            usingCount = min(amount//v, c)
            res[itr] += usingCount
            amount -= usingCount*v
        
        if amount>0:
            print(f"NO WITHDRAW")
            return [-1]
        
        for itr in range(5):
            self.count[itr] -= res[itr]
        print(f"WITHDRAW: {self.count}")
        return res
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)