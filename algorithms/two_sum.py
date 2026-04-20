#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for index, item in enumerate(nums):
        complement = target - item
        if complement in seen:
            return [index, seen[complement]]
        seen[item] = index

nums = [5,0,1]
target = 6
print(twoSum(nums, target))
