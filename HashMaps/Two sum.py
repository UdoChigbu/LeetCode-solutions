from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #making hashmap
        hashMap = {}
        
    
        for i, num in enumerate(nums):
            addend = target-num
            
            if addend in hashMap:
                return [hashMap[addend], i]
            hashMap[num] = i
        return[]
            

            

            
solution = Solution()
array = solution.twoSum([3,2,4], 6)
for index in array:
    print(index)

            
                