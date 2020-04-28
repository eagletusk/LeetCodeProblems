
'''
public int removeDuplicates(int[] nums) {
        
  // Check for edge cases.
  if (nums == null) {
      return 0;
  }
  
  // Use the two pointer technique to remove the duplicates in-place.
  // The first element shouldn't be touched; it's already in its correct place.
  int writePointer = 1;
  // Go through each element in the Array.
  for (int readPointer = 1; readPointer < nums.length; readPointer++) {
      // If the current element we're reading is *different* to the previous
      // element...
      if (nums[readPointer] != nums[readPointer - 1]) {
          // Copy it into the next position at the front, tracked by writePointer.
          nums[writePointer] = nums[readPointer];
          // And we need to now increment writePointer, because the next element
          // should be written one space over.
          writePointer++;
      }
  }
  
  // This turns out to be the correct length value.
  return writePointer;
}
'''

# convert to python

def removeDuplicates(nums):
  if nums == None:
    return 0 

  print(nums)
  write_pointer = 1

  for i in range(1,len(nums),1):
    if nums[i] != nums[i-1]:
      nums[write_pointer] = nums[i]
      write_pointer +=1

  print(nums)
  return nums[0:write_pointer]

print(removeDuplicates([0,0,1,1,1,1,3,4,5,5]))