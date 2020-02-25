def find_triplets(nums):
    if len(nums) < 3:
        return []

    return_list = []
    while nums:
        first = nums.pop(0)
        list_len = len(nums)
        i = 0
        while i < len(nums):
             second = nums[i]
             third = 0 - (first + second)
             if third in nums[0:i] + nums[i+1:]:
                 return_list.append([first, second, third])
                 nums.remove(second)
                 nums.remove(third)
             i += 1
        return return_list

list1 = [-1, 0, 1, 2, -1, -4]
print find_triplets(list1)
list1 = [1,2,-2,-1]
