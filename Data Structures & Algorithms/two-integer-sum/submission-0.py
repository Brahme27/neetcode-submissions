class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict={}
        for i in range(len(nums)):
            remaining=target-nums[i]
            if remaining in mydict:
                return [mydict[remaining],i]
            mydict[nums[i]]=i    