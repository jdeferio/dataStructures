import copy

# determine if a array is in ascending order
def is_ascending(nums: list) -> bool:
    if nums == sorted(nums):
        return True
    return False

# determine if an array can be made ascending if 1 item is removed
def can_be_made_ascending(nums: list) -> bool:
    if is_ascending(nums):
        return True
    for i, n in enumerate(nums):
        v_nums = copy.deepcopy(nums).pop(i)
        if is_ascending(v_nums):
            return True
        return False

