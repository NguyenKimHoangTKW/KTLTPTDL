def searchRange(nums, target):
    def search(nums, target, left):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    left_idx = search(nums, target, True)

    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]

    return [left_idx, search(nums, target, False) - 1]
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(f"Dãy nhận vào là {nums1}")
print(f"Đích : {target1}")
print("Ví trí bắt đầu và kết thúc của giá trị đích là : ",searchRange(nums1, target1))

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(f"Dãy nhận vào là {nums2}")
print(f"Đích : {target2}")
print("Ví trí bắt đầu và kết thúc của giá trị đích là : ",searchRange(nums2, target2))

nums3 = []
target3 = 0
print(f"Dãy nhận vào là {nums3}")
print(f"Đích : {target3}")
print("Ví trí bắt đầu và kết thúc của giá trị đích là : ",searchRange(nums3, target3))

