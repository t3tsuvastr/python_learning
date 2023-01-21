# Condition
# n schoolchildren divide k apples equally, the non-divisible remainder remains in the basket.
# How many apples will each student get? How many apples will be left in the basket?
# The program receives the numbers n and k as input and must output the desired number of apples (two numbers).

n = int(input())
k = int(input())
print('received apples:', k//n)
print('remainder:', k%n)