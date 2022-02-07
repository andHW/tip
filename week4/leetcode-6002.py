# https://leetcode.com/contest/weekly-contest-279/problems/design-bitset/
class Bitset:

    def __init__(self, size: int):
        self.bs = [0]*size
        self.size = size
        self.v = 0
        self.mask = 2**size-1

    def fix(self, idx: int) -> None:
        self.v |= (1 << (self.size-1-idx))

    def unfix(self, idx: int) -> None:
        self.v &= ~(1 << (self.size-1-idx))

    def flip(self) -> None:
        self.v = ~self.v & self.mask

    def all(self) -> bool:
        return self.v == self.mask

    def one(self) -> bool:
        return self.v != 0

    def count(self) -> int:
        return self.v.bit_count()

    def toString(self) -> str:
        return f'{self.v:0{self.size}b}'


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
