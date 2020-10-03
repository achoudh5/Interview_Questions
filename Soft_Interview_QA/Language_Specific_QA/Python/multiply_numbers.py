# Intern Level Interview Question
# 
# Question
# Without using the multiply function (*) multiply togeather two given numbers

# Answer - Basic
# If get this quickly ask extension
# Two variables to multiply
a = 3
b = 5

# Result variable
result = 0

for x in range(a):
	result += b

print (result)

# Question - extension
# Given that the previous answer works, how could we extend the answer to cope with one or both inputs being a negative value?

# Answer - extension
c = -4
d = 5

negative = False
result = 0

# Check if negative for one or both, toggle to keep LoC low
if c < 0:
	negative = not negative

if d < 0:
	negative = not negative

# Use abs to remove the negative
for y in range(abs(c)):
	result += abs(d)

# If still needs to be negative, make result negative
if negative:
	result = -result

print(result)
