from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = 0

        while left < right:
            distance = abs(right - left)
            minimumHeight = min(height[left], height[right])
            maxArea = max(maxArea, minimumHeight*distance)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea
      

                     
                     


            

                
    
solution = Solution()
result = solution.maxArea([1,1])
print(result)