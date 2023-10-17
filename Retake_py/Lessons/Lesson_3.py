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
