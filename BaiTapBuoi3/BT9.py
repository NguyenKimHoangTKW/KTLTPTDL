def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums1 = [2, 2, 1]
print(singleNumber(nums1)) 

nums2 = [4, 1, 2, 1, 2]
print(singleNumber(nums2)) 

nums3 = [1]
print(singleNumber(nums3)) 
