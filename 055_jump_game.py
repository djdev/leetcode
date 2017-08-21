# -*- coding: utf-8 -*-
"""
55. Jump Game

Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution(object):
    # http://www.cnblogs.com/zuoyuan/p/3781933.html
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False

        return True

    # https://www.hrwhisper.me/leetcode-jump-game/
    """
    cover表示当前覆盖到的下标，
    如果cover >=len(A)-1，说明跳到了目的地，有解。
    否则，每一次只要cover >=i ，即可判断是否可以更新cover
    """
    def canJump(self, nums):
        cover = 0
        # for i, x in enumerate(nums):
        for i in range(len(nums)):
            if cover >= len(nums) - 1:
                return True
            if cover >= i:
                cover = max(cover, nums[i] + i)
        return False



if __name__ == '__main__':
    print Solution().canJump([2, 3, 1, 1, 4])