# You are given an array of integers nums. You must calculate the product of the elements in a specific "middle-out" order. The traversal starts at the middle element and then alternates between the element to its left and the element to its right, moving outwards.
# If nums has an even number of elements, the traversal starts with the left of the two middle elements. Return the final product.
nums = [4, 5, 6, 7, 8]
def f(nums):
    new_order = []
    product = 1
    mid = len(nums) // 2
    if len(nums) % 2 == 1:
        left = mid - 1
        right = mid + 1
        new_order.append(nums[mid])
    else:
        left = mid - 1
        right = mid
        new_order = []
    while left >= 0 and right < len(nums):
        new_order.append(nums[left])
        new_order.append(nums[right])
        left -= 1
        right += 1
    for i in new_order:
        product *= i
    return product

print(f(nums))
