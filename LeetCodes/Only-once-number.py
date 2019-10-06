'''给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。'''
'''方法 1：列表操作

算法

    遍历 nums 中的每一个元素
    如果某个 nums 中的数字是新出现的，则将它添加到列表中
    如果某个数字已经在列表中，删除它'''
class Solution(object):
	def getOnceNumber(self,nums):
		duplicate = []
		for i in nums:
			if i not in duplicate:
				duplicate.append(i)
			else:duplicate.remove(i)
		return duplicate.pop()
m = [2,4,2,5,6,7,5,6,4]
print(Solution().getOnceNumber(m))
