class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x,y,r in circles:
            rSquare = r**2
            for mx in range( x-r, x+r+1 ):
                for my in range( y-r, y+r+1 ):
                    if (mx-x)**2+(my-y)**2 <= rSquare:
                        points.add((mx,my))
        print(points)
        return len(points)
            