class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of_the_number = {

        }
        for i in range(0, len(nums)):
            index_of_the_number[nums[i]] = i
        for i in range(0, len(nums)):
            complement = target-nums[i]
            if (complement in index_of_the_number) and index_of_the_number[complement] != i:

                return [i, index_of_the_number[complement]]
