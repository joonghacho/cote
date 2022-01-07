from typing import List

class Solution:
    def max_sum_of_one(self, sub_sums, one_len):
        if len(sub_sums) <= one_len:
            return sum(sub_sums)
        max_sum = 0
        for i in range(one_len):
            max_sum += sub_sums[i]
        current_sum = max_sum
        for i in range(len(sub_sums) - one_len):
            current_sum -= sub_sums[i]
            current_sum += sub_sums[i + one_len]
            if (current_sum > max_sum):
                max_sum = current_sum
        return max_sum

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        max_sum = 0
        final_result = 0
        first_result = 0
        second_result = 0

        for i in range(firstLen):
            first_result += nums[i]
        max_sum += first_result
        max_sum += self.max_sum_of_one(nums[firstLen:], secondLen)
        for i in range(len(nums) - firstLen):
            first_result -= nums[i]
            first_result += nums[i + firstLen]
            left_second_result = self.max_sum_of_one(nums[:i+1], secondLen)
            second_result = left_second_result
            right_second_result = self.max_sum_of_one(nums[i+1+firstLen:], secondLen)
            if (right_second_result > left_second_result):
                second_result = right_second_result
            final_result = first_result + second_result
            if (final_result > max_sum):
                max_sum = final_result
        return max_sum

sub_sums_1 = [20,16,5,2,6,0,7,0,12,6,15,7,13,6,8,19,2,2,4]
solution = Solution()
print(solution.maxSumTwoNoOverlap(sub_sums_1, 1, 7))