def in_order_diff_three_strict(nums):
    if not nums:
        return True
    elif len(nums) == 1:
        return True
    else:
        low_to_high = True
        if nums[0] > nums[1]:
            low_to_high = False
        prev = nums[0]
        for i in range(1, len(nums)):
            if not (1 <= abs(prev - nums[i]) <= 3):
                return False
            if low_to_high and prev > nums[i]:
                return False
            if not low_to_high and prev < nums[i]:
                return False
            prev = nums[i]
    return True


def find_safe_report_strict(path):
    ans = 0
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            elem = [int(s) for s in line.split(" ")]
            print(elem)
            if in_order_diff_three_strict(elem):
                ans += 1
    return ans


def in_order_diff_three_one_error(nums):
    num_errors = 0
    if not nums:
        return 1
    elif len(nums) == 1:
        return 1
    else:
        go_to_next = True
        low_to_high = True
        if nums[0] > nums[1]:
            low_to_high = False
        prev = nums[0]
        i = 1
        while i < len(nums):
            
    if num_errors == 1:
        return 0
    else:
        return 1


def find_safe_report_one_error(path):
    ans = 0
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            elem = [int(s) for s in line.split(" ")]
            print(elem)
            if in_order_diff_three_strict(elem) in [0, 1]:
                ans += 1
    return ans


# print(find_safe_report_strict("dayTwoInput.txt"))
print(find_safe_report_one_error("dayTwoInput.txt"))
