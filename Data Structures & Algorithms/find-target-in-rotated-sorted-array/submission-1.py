from typing import List

class Solution:
    def find_pivot(self, nums: List[int]) -> int:
       
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return l

    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        pivot = self.find_pivot(nums)

        if target >= nums[pivot] and target <= nums[-1]:
            left, right = pivot, len(nums) - 1
        else:
            left, right = 0, pivot - 1

        return self.binary_search(nums, left, right, target)