class Solution:
	# 在Olog(n)的时间复杂度下，实现x的n次方

	def pow(self, x, n):
		if x == 0:
			return 0

		negative = False

		if n == 0:
			return 1
		elif n < 0:
			negative = True
			n = -n

		res = self.pow_function(x, n)

		if negative:
			res = 1 / res
		return res

	def pow_function(self, x, n):
		if n == 1:
			return x

		# 使用右移1代替除以2
		tmp = self.pow_function(x, n >> 1) * self.pow(x, n >> 1)

		if n % 2 == 1:
			tmp = x * tmp

		return tmp

if __name__ == '__main__':

	res = Solution().pow(2, 7)
	print(res)

