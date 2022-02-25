#The Question:
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#

# The First Solution Is With Time Complexity Of O(n²) and Space Complexity Of O(1)
# The Brute Force Solution:
def twoSum(nums,target):
    if len(nums) <=104 and len(nums)>=2 and target >=-109 and target <=109:
        for i in range(0,len(nums)):
             for j in range(0,len(nums)):
                if j==i:
                     continue
                else:
                    if nums[i]+nums[j]== target:
                        return f"Output: [{i},{j}]"


print(twoSum([2,7,11,15],10))

# The Second Solution Is With Time Complexity Of O(n) and Space Complexity Of O(n)