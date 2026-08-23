from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)      # O(n)
        longest = 0

        for x in num_set:
            # Only start counting if x is the beginning of a sequence
            if x - 1 not in num_set:
                current_length = 1
                current_num = x

                # Count how far the streak goes
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest