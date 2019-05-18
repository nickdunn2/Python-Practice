nums1 = [1, 3, 7, 5, 9]
nums2 = [2, 4, 6, 8, 10]


def mini_max_sum(arr):
    arr.sort()
    return f"{sum(arr[:-1])} {sum(arr[1:])}"


print(mini_max_sum(nums1))
print(mini_max_sum(nums2))
