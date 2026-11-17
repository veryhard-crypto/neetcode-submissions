class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        m = 0
        def swap(i,j):
            temp = nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        while m <= r:
            if nums[m] == 0:
                swap(l,m)
                l+=1
            elif nums[m] == 2:
                swap(r,m)
                r-=1
                m-=1
            m+=1