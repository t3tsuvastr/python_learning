# Condition
# Number n is given. N minutes have passed since the beginning of the day.
# Determine how many hours and minutes the digital clock will show at this moment.
# The program should output two numbers:
# the number of hours (from 0 to 23) and the number of minutes (from 0 to 59).
# Note that the number n can be greater than the number of minutes in a day.

n = int(input())
h = n // 60 - ((n // 60) // 24) * 24
m = n % 60
print (h , m)