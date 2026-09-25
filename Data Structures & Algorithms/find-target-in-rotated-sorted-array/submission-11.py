class Solution:
    def search(self, nums: List[int], target: int) -> int:
        onums = list(nums)
        # find where the array splits
        offset = 0
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target: return 0
            return -1
        if len(nums) == 2:
            if nums[0] == target: return 0
            if nums[1] == target: return 1
            else: return -1
        while len(nums) > 0:
            i = len(nums) // 2
            p = nums[i]
            if len(nums) == 2:
                if nums[0] > nums[1]:
                    offset += 1
                break
            elif p > nums[-1]:
                # right
                offset += i
                nums = nums[i:]
            else:
                # left
                nums = nums[:i+1]
        lnums = onums[:offset]
        rnums = onums[offset:]
        nums = lnums
        # search for the number in the left part
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
        # search for the number in the right part
        nums = rnums
        offset = len(lnums)
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