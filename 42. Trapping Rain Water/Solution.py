class Solution:
    def trap(self, height: List[int]) -> int:
        
        result = 0
        left_index = 0
        right_index = len(height)-1
        left_max = 0
        right_max = 0
        
        while left_index < right_index:
            left_max = max(left_max, height[left_index])
            right_max = max(right_max, height[right_index])
            
            if left_max <= right_max:
                result += (left_max - height[left_index])
                left_index += 1
            else:
                result += (right_max - height[right_index])
                right_index -= 1
        return result
        
        
   '''
   Reference Links:
   1) https://www.youtube.com/watch?v=BRrHqmzvln8
   2) https://youtu.be/W-lWBEVE7Uc?t=635
   '''
