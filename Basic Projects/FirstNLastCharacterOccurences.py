class FirstLastOccurences():

    def get_lower_bound(self, nums, target):
        print(nums)
        low, high = 0, len(nums)-1
        ans = -1
        #applying binary search to find the lower_bound
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                ans = mid
                high = mid-1 #iterate until find the first occurence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
    def get_upper_bound(self, nums, target):
        #applying binary search to find the upper_bound
        low, high = 0, len(nums)-1
        ans = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                ans = mid
                low = mid+1 #iterate until find the last occurence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans
        
    def searchRange(self, nums, target):

        if not nums:
            return [-1, -1]
            
        lower_bound = self.get_lower_bound(nums, target)
        #rev_num = nums[::-1] 
        upper_bound = self.get_upper_bound(nums, target)
        #upper_bound = self.get_lower_bound(rev_num,target)
        return [lower_bound, upper_bound]
        
if __name__ == "__main__":
    f = FirstLastOccurences()
    arr = [1,2,3,4,4,4,4,5,5,5,5,5,5,5,7,7,7,8,9]
    #arr = [5,5,5,5,5,5,5,5] #checkworstcase
    first,sec = f.searchRange(arr,5)
    print(first)
    print(sec)