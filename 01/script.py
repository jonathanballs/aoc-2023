#
# Part 1
#
calibration_sum = 0

for line in  open('./input', 'r+'):
    nums = [c for c in line if c in '0123456789']
    calibration_value = (int(nums[0]) * 10) + int(nums[-1])
    calibration_sum += calibration_value

print("part 1: ", calibration_sum)

#
# Part 2
#
num_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_dict = {}
for i in range(len(num_strings)):
    num_dict[num_strings[i]] = i + 1
    num_dict[str(i + 1)] = i + 1

calibration_sum = 0

for line in  open('./input', 'r+'):
    num_indices = {}
    for num in num_dict.keys():
        if line.find(num) != -1:
            num_indices[line.find(num)] = num_dict[num]
            num_indices[line.rfind(num)] = num_dict[num]

    first_num = num_indices[min(num_indices.keys())]
    last_num = num_indices[max(num_indices.keys())]

    calibration_value = first_num * 10 + last_num
    calibration_sum += calibration_value

print("part 2: ", calibration_sum)
