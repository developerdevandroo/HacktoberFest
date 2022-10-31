# Python3 program for the above approach
from math import ceil, sqrt

# Function to check if a
# number is prime or not
def isPrime(n):
	
	# If n is less than
	# or equal to 1
	if (n <= 1):
		return False

	# If n is less than
	# or equal to 3
	if (n <= 3):
		return True

	# If n is a multiple of 2 or 3
	if (n % 2 == 0 or n % 3 == 0):
		return False

	# Iterate over the range [5, n]
	for i in range(5, ceil(sqrt(n)), 6):
		
		# If n is a multiple of i or (i + 2)
		if (n % i == 0 or n % (i + 2) == 0):
			return False

	return True

# Function to count the required
# numbers from the given range
def cntNum(pos, st, tight, prime):
	
	global dp, num
	
	if (pos == len(num)):
		return 1

	# If the subproblems already computed
	if (dp[pos][st][tight][prime] != -1):
		return dp[pos][st][tight][prime]

	res = 0

	# Stores maximum possible
	# at current digits
	end = num[pos] if (tight == 0) else 9

	# Iterate over all possible digits
	# at current position
	for i in range(end + 1):
		
		# Check if i is the maximum possible
		# digit at current position or not
		ntight = 1 if (i < end) else tight

		# Check if a number contains
		# leading 0s or not
		nzero = 1 if (i != 0) else st

		# If number has only leading zeros
		# and digit is non-zero
		if ((nzero == 1) and isPrime(i) and
							isPrime(prime)):
								
			# Prime digits at prime positions
			res += cntNum(pos + 1, nzero, ntight,
						prime + 1)

		if ((nzero == 1) and isPrime(i) == False and
						isPrime(prime) == False):

			# Non-prime digits at
			# non-prime positions
			res += cntNum(pos + 1, nzero, ntight,
						prime + 1)

		# If the number has only leading zeros
		# and i is zero,
		if (nzero == 0):
			res += cntNum(pos + 1, nzero,
						ntight, prime)
						
	dp[pos][st][tight][prime] = res
	
	return dp[pos][st][tight][prime]

# Function to find count of numbers in
# range [0, b] whose digits are prime
# at prime and non-prime at non-prime pos
def cntZeroRange(b):
	
	global num, dp

	num.clear()
	
	while (b > 0):
		num.append(b % 10)
		b //= 10

	# Reversing the digits in num
	num = num[::-1]

	# print(num)
	dp = [[[[-1 for i in range(19)]
				for i in range(2)]
				for i in range(2)]
				for i in range(19)]

	res = cntNum(0, 0, 0, 1)

	# Returning the value
	return res

# Driver Code
if __name__ == '__main__':

	dp = [[[[-1 for i in range(19)]
				for i in range(2)]
				for i in range(2)]
				for i in range(19)]
	L, R, num = 5, 22, []

	# Function Call
	res = cntZeroRange(R) - cntZeroRange(L - 1)

	# Print answer
	print(res)

# This code is contributed by mohit kumar 29
