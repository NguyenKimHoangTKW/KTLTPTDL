def singleNumber(nums):
    result = 0
    for i in range(32):
        count = 0
        for num in nums:
            count += (num >> i) & 1
        result |= (count % 3) << i
    if result >= 2**31:
        result -= 2**32
    return result

nums1 = [2, 2, 3, 2]
print(singleNumber(nums1)) 

nums2 = [0, 1, 0, 1, 0, 1, 99]
print(singleNumber(nums2))
