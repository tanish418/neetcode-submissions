class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n==1:
            return nums

        m=len(nums)//2
        l_nums = nums[:m]    
        r_nums = nums[m:]   

        L = self.sortArray(l_nums) 
        R = self.sortArray(r_nums) 

        l,r = 0,0
        L_len,R_len = len(L),len(R)

        sorted_array = [0]*n
        i=0
        while l<L_len and r<R_len:
            if L[l]<R[r]:
                sorted_array[i]=L[l]
                l+=1
            else:
                sorted_array[i]=R[r]
                r+=1
            i+=1       
        while l<L_len:
            sorted_array[i]=L[l]
            l+=1
            i+=1
        while r<R_len:
            sorted_array[i]=R[r]
            r+=1
            i+=1
        return sorted_array