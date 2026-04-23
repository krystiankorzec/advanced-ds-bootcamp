nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    nums.sort()
    triplets = []
    for i, el in enumerate(nums):
        # check if duplicate
        if (i > 0) and (el == nums[i-1]):
            continue    
        left = i+1
        right = len(nums) - 1
        target = -1*el
        while right > left:
            current_sum = nums[left] + nums[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                left = left +1
                while (right > left) and (nums[left] == nums[left -1]):
                    left +=1
    return triplets
threeSum(nums)

for i, el in enumerate(nums):
    left = i
    right = len(nums) - 1
    target = -1*el
    print(f"target is {target}")
    print(f"left is {left}")
    print(f"right is {right}")
    print(f"current sum is {nums[left] + nums[right]}")

i=1
left=2
right=5
target=1
triplets = []
while right > left:
    current_sum = nums[left] + nums[right]
    if current_sum > target:
        right -= 1
    elif current_sum < target:
        left += 1
    else:
        triplets.append([nums[i], nums[left], nums[right]])
        print(triplets)
        left = i + 1
        right= len(nums)-1