from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in num_dict:
                return [num_dict[y], i]
            num_dict[x] = i
        return []


# 测试用例
def run_tests():
    sol = Solution()

    # 基本测试
    print(sol.twoSum([2, 7, 11, 15], 9))  # 应该返回 [0, 1]

    # 数组中有重复元素
    print(sol.twoSum([3, 3], 6))  # 应该返回 [0, 1]

    # 目标和由数组中的第一个和最后一个元素组成
    print(sol.twoSum([1, 2], 3))  # 应该返回 [0, 1]

    # 没有结果，目标和不在数组中任何两个元素之和中
    print(sol.twoSum([1, 2, 4, 7], 8))  # 应该返回 []

    # 数组中只有一个元素
    print(sol.twoSum([1], 2))  # 应该返回 []

    # 数组为空
    print(sol.twoSum([], 1))  # 应该返回 []


run_tests()