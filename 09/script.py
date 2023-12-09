integral_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split('\n')

integral_input = open('./input').read().strip().split('\n')

def differentiate(nums):
    ret = [0] * (len(nums)-1)
    for i in range(len(ret)):
        ret[i] = nums[i+1] - nums[i]
    return ret

def is_all_zeroes(nums):
    return nums == [0]*len(nums)

def find_next_integer(nums):
    if is_all_zeroes(nums):
        return 0
    return nums[-1] + find_next_integer(differentiate(nums))

next_val_sum = 0
for line in integral_input:
    vals = [int(n) for n in line.split()]
    next_val_sum += find_next_integer(vals)

print("Part 1:", next_val_sum)

prev_val_sum = 0
for line in integral_input:
    vals = [int(n) for n in line.split()]
    vals.reverse()
    prev_val_sum += find_next_integer(vals)

print("Part 2:", prev_val_sum)
