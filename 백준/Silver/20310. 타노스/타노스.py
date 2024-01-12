nums = list(input())

zero, one = 0,0
for n in nums:
    if n == '0':
        zero += 1
    else:
        one += 1

zero //= 2
one //= 2

tmp = []
while zero:
    tmp.append('0')
    zero -= 1

while one:
    tmp.append('1')
    one -= 1

tmp.sort()
print(''.join(tmp))