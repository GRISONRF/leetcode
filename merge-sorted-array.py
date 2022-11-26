""" You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


this answer just take up the empty numbers in the array m and add the numbers of the array n, and at the end use sort.

time complexity is O(n log n) because of the sort  
space complexity is O(N) worst case, O(1) best case, because sort does not create an additional array, it sorts in place"""



def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    j = 0
    for i in range(m, m + n):
        nums1[i] = nums2[j]
        j += 1
    
    return nums1.sort()
    
   

print(merge([1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))