# 401. Binary Watch

# A binary watch has 4 LEDs on the top which represent the hours (0-11),
# and the 6 LEDs on the bottom represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on,
# return all possible times the watch could represent.
#
# Example:
#
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
#
# Note:
#
#     The order of output does not matter.
#     The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
#     The minute must be consist of two digits and may contain a leading zero,
# for example "10:2" is not valid, it should be "10:02".

class Solution(object):
    # http://bookshadow.com/weblog/2016/09/18/leetcode-binary-watch/
    # 位运算（Bit Manipulation）
    # 10盏灯泡的燃亮情况可以通过0-1024进行表示，然后计数二进制1的个数即可。
    # 利用位运算将状态拆分为小时和分钟。
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for x in range(1024):
            if bin(x).count('1') == num:
                h, m = x >> 6, x & 0x3F
                if h < 12 and m < 60:
                    ans.append('%d:%02d' %(h, m))
        return ans

    # 枚举小时h和分钟m，然后判断二进制1的个数是否等于num
    def readBinaryWatch(self, num):
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    ans.append('%d:%02d' %(h, m))
        return ans

test = Solution()
print(test.readBinaryWatch(1))
print(test.readBinaryWatch(5))

