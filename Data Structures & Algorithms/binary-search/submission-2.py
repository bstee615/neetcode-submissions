class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = 0
        while len(nums) > 0:
            i = len(nums) // 2
            p = nums[i]
            if p == target:
                return offset + len(nums) // 2
            else:
                if p > target:
                    # left
                    nums = nums[:i]
                else:
                    # right
                    offset += i+1
                    nums = nums[i+1:]
        return -1