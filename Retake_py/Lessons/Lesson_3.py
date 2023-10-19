# def twoSum(nums, target):
#     length_of_nums = len(nums)
#     before_first_after_last = length_of_nums - 1

#     for i in range(before_first_after_last):
#         next_element_to_the_last_element = i + 1
#         for j in range(next_element_to_the_last_element, length_of_nums):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     target_not_found = []

#     return target_not_found


# print(twoSum([2, 7, 11, 15], 9))

# def isPalindrome(x:str):
#     to_str = str(x)
#     return to_str == to_str[::-1]

# print(isPalindrome(121))


# def lengthOfLongestSubstring(s):
#         seen = {}
#         l = 0 
#         length = 0
#         for r in range(len(s)):
#             char = s[r]
#             if char in seen and seen[char] >= l:
#                 l = seen[char] + 1
#             else:
#                 length = max(length, r - l + 1)
#             seen[char] = r
        
#         return length

# print(lengthOfLongestSubstring('pwwkew'))


# 
# def removeElement(nums:list, val):
    # i = 0
    # for x in nums:
    #     if x != val:
    #         nums[i] = x
    #         i += 1
    # return i
    
#     result = []
#     removItems = []
#     for items in nums:
#         if items == val:
#             result.append('_')
#         else:
#             removItems.append(items)        
#     return len(removItems)




# print(removeElement([0,1,2,2,3,0,4,2], 2))

# import time

# start_time = time.time()
# for i in range(100):
#     for i2 in range(100):
#         print(i2)
# end_time = time.time()

# print("Time take: ",  round(end_time - start_time, 4))
# print(start_time, end_time)



# itr1 = ['a', 'b', 'c']
# itr2 = [1, 2, 3]
# itr3 = ['x', 'y', 'z']
# zipped_itr = zip(itr1, itr2, itr3)

# for i in zipped_itr:


# import random

# letters = 'abcdejfalskrjn' 
# letters_ru = 'пфыдткогвау'
# numbers = '1234567890'
# sumbols = '!@#$%^&*'

# total_symbols = 20

# every = letters + letters_ru + numbers + sumbols
# creater = ''

# for i in range(total_symbols): 
#     random_int = random.randint(0, len(every) - 1)
#     creater += every[random_int]



# print(creater)


