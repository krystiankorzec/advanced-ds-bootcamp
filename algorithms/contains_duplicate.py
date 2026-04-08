from typing import List
def contains_duplicate(nums:List) -> bool:
    '''
    Checks if list contains duplicated elements. 
    Returns True if there are duplicates.
    '''
    return len(nums) != len(set(nums))

if __name__ == "__main__":
    nums = [1,1,2,3,4]
    assert contains_duplicate(nums) is True
    nums2 = [4,5]
    assert contains_duplicate(nums2) is False
    print("All tests passed!")