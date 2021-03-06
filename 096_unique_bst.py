# -*- coding: utf-8 -*-
"""
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

http://www.cnblogs.com/zuoyuan/p/3747824.html

解题思路：这题从数学上讲，其实是明安图-卡特兰数。
不过我们显然不从数学上来解决这个问题。
这题是求二叉树的棵数。
这里有个解题技巧：一般来说求数量，要首先想到使用动态规划（dp），
而如果是像下一题的要求，不只是数量，还要把所有的树都枚举出来，就要使用dfs（深度优先搜索）来遍历决策树了。

这道题是使用动态规划来解决的。
那么如何去求这个问题的状态转移方程呢？
其实大部分动态规划的难点都是求状态转移方程。
n=0时，为空树，那么dp[0]=1;
n=1时，显然也是1，dp[1]=1；
n=2时，dp[2]=2;
对于n>2时，
dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2] +...... + dp[n-2]*dp[1] + dp[n-1]*dp[0]
这不就是明安图-卡特兰数的定义吗？编程很容易实现。

"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for _ in range(n - 2)]
            for i in range(3, n + 1):
                for j in range(i):
                    # j: left nodes number
                    # i-j-1: right nodes number (excluding root node)
                    dp[i] += dp[j] * dp[i - j - 1]
            return dp[n]

    # https://gengwg.blogspot.com/2018/03/leetcode-96-unique-binary-search-trees.html
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]


if __name__ == '__main__':
    print Solution().numTrees(5)
