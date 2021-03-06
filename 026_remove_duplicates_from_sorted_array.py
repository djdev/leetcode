"""
26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place
such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this in place with constant memory.

For example,

Given input array nums = [1,1,2],

Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

https://github.com/gengwg/leetcode
"""
# Time:  O(n)
# Space: O(1)
#


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # return len(set(nums))

        if not nums:
            return 0

        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                # exchange n[i] <--> n[j+1]; j+1, not j!
                nums[i], nums[j + 1] = nums[j + 1], nums[i]
                j += 1
        # j now points to the last distinct element index
        return j + 1

    def removeDuplicates(self, A):
        if not A:
            return 0

        # maintain two pointers
        # last points to the last position of distinct elements
        # i iterate over all elements
        # when see a different element, increment last, and set its value to the new element
        # this works because array is sorted
        last, i = 0, 1
        while i < len(A):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
            i += 1
        # array length is last index + 1
        return last + 1

    def removeDuplicates(self, A):
        if not A:
            return 0

        last = 0
        for i in range(1, len(A)):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]

        return last + 1


    def removeDuplicatesExtraSpace(self, nums):

        duplicates = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                duplicates.append(nums[i])

        for d in duplicates:
            nums.remove(d)

        return len(nums)

if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 2, 2, 3])
    print Solution().removeDuplicates([1, 1])
    print Solution().removeDuplicates([1, 1, 1, 1])
