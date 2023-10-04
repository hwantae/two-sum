from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    ind = {}
    for i, num in enumerate(nums):
        remain = target - num
        if remain in ind:
            return [ind[remain], i]
        ind[num] = i
    return