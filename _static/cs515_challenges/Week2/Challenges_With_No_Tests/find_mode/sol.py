# define find_mode(nums)
def find_mode(nums):
    # Handle base cases in O(1)
    if nums == []: return None
    elif len(nums) == 1: return nums[0]
    elif len(nums) == 2: return nums
    else:
        new_dict = {}
        for item in nums:
            if item in new_dict:
                new_dict[item] += 1
            else: new_dict[item] = 1
        m = max(new_dict.values())
        return list(new_dict.keys())[list(new_dict.values()).index(m)]
        
# here are some tests

assert find_mode([5, 5, 6, 4, 7, 8, 5, 6]) == 5
assert find_mode([1,1,1,2,2,2,2]) == 2
assert find_mode([]) == None