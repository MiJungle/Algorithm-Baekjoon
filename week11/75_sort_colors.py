

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)
        while white < blue:
            if nums[white]<1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue-= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white +=1
 


#쉬운 풀이
#  class Solution(object):
#     def sortColors(self, nums):
#         return nums.sort()


# Runtime: 35 ms, faster than 29.35% of Python online submissions for Sort Colors.
# Memory Usage: 13.6 MB, less than 14.33% of Python online submissions for Sort Colors.
