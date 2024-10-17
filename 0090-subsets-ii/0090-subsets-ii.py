class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        max_num = max(nums)
        min_num = min(nums)
        countmap = [0]*(max_num-min_num+1)
        ## Could have also used a hashmap instead of countmap
        n = len(countmap)
        for num in nums:
            countmap[num - min_num] += 1
        print(countmap)
        def subset(curr_set,size,idx,curr_countmap):
            if len(curr_set) == size:
                ans.append(curr_set)
            else:
                for i in range(idx,n):
                    if curr_countmap[i] > 0:
                        num = min_num + i
                        new_set = curr_set + [num]
                        curr_countmap[i] -= 1
                        subset(new_set,size,i,curr_countmap)
                        curr_countmap[i] += 1
        for i in range(len(nums)+1):
            subset([],i,0,countmap)
        return ans
        