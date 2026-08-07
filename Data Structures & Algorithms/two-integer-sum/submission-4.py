class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        myhash={}
        for index,num in enumerate(nums):
            diff=target-num 
            if diff in myhash:
                return [myhash[diff],index]
            myhash[num]=index