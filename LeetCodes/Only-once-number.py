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

'''方法 2：哈希表

算法

我们用哈希表避免每次查找元素是否存在需要的 O(n)O(n)O(n) 时间。

    遍历 nums 中的每一个元素
    查找 hash_tablehash 中是否有当前元素的键
    如果没有，将当前元素作为键插入 hash_tablehash
    最后， hash_tablehash 中仅有一个元素，用 popitem 获得它

'''
class Solution1(object):
	def getOnceNumber(self,nums):
		