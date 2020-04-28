from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_p = len(nums)-1 # 7
        head_p = 0

        # if (len(nums)== 0)
          

        while head_p < write_p+1:
          if nums[head_p] == 0:
            # move all elements over 1 place
            # place 0 at end
            for i in range(head_p+1,write_p+1,1): # 7
              #  print(nums,i,write_p)
               nums[i-1] = nums[i]
            head_p -=1
            nums[write_p] = 0
            write_p -=1  
          head_p +=1
        


sol = Solution()
print(sol.moveZeroes([0,1,3,12,0,23]))

