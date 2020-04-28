
from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result =[]
        for i in A:
            result.append(i*i)
        result.sort()
        return result

sol = Solution()
print(sol.sortedSquares([2,3,4,5,23]))
print(sol.sortedSquares([3,1,2,4]))
