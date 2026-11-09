class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create an empty dictionary
        seen = {}

        # Visit each number using its index
        for i in range(len(nums)):

            # Find the missing number
            complement = target - nums[i]

            # Check whether the missing number exists
            if complement in seen:

                # Return both indexes
                return [seen[complement], i]

            # Store the number and its index
            seen[nums[i]] = i
