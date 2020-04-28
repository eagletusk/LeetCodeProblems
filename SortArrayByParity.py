from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
      
      h = 0
      end = len(A)-1
      temp = 0
      j=0
      i=0
      while i < end:
        if A[i] %2 != 0:
          # odd
          temp = A[i]

        # shift every thing over
          j = i+1
          while j <=end:
            A[j-1] = A[j]
            j+=1
          # print(A)

          A[end] = temp
          end-=1
          i-=1
          # print(A)
        i+=1
      return A

        

sol = Solution()
print(sol.sortArrayByParity([2,3,4,5,23]))
print(sol.sortArrayByParity([3,1,2,4]))
# 41245230