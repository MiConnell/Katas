# https://leetcode.com/problems/two-sum/
"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = sorted(nums) if sorted(nums) != nums else nums
        left = 0
        right = len(n) - 1
        while left < right:
            curr = n[left] + n[right]
            if curr < target:
                left += 1
            elif curr > target:
                right -= 1
            else:
                if sorted(nums) != nums:
                    return [nums.index(n[left]), nums.index(n[right])]
                else:
                    return [left, right]
        return [-1, -1]
