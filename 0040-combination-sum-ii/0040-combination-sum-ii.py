class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # ans = []
        # ans_set = set()
        # min_candidates = min(candidates)
        # max_candidates = max(candidates)
        # countmap = [0]*(max_candidates - min_candidates + 1)
        # for num in candidates:
        #     countmap[num - min_candidates] += 1
        # def backtrack(curr_list,curr_sum,curr_map):
        #     if curr_sum > target:
        #         return
        #     if curr_sum == target:
        #         curr_list.sort()
        #         sorted_tuple = tuple(curr_list)
        #         if sorted_tuple not in ans_set:
        #             ans_set.add(sorted_tuple)
        #             ans.append(curr_list)
        #             return
        #     else:
        #         for i in range(len(curr_map)):
        #             if curr_map[i] > 0:
        #                 curr_map[i] -= 1
        #                 curr_num = min_candidates + i
        #                 new_list = curr_list + [curr_num]
        #                 new_sum = curr_sum + curr_num
        #                 backtrack(new_list,new_sum,curr_map)
        #                 curr_map[i] += 1
        # backtrack([],0,countmap)
        # return ans

        ## Solution below is clearer

        candidates.sort()
        ans = []
        def backtrack(curr_list,curr_sum,idx):
            if curr_sum > target:
                return
            elif curr_sum == target:
                ans.append(curr_list)
                return
            else:
                ## set it to any number outside the range of valid candidates
                prev = -1 
                for i in range(idx,len(candidates)):
                    ## This condition means that only the first element in the 
                    ## current iteration of backtracking is allowed to have
                    ## consecutive same elements, in which the consecutive streak
                    ## of the first element began before the current iteration
                    if candidates[i] == prev:
                        continue
                    new_list = curr_list + [candidates[i]]
                    new_sum = curr_sum + candidates[i]
                    backtrack(new_list,new_sum,i+1)
                    prev = candidates[i]
        backtrack([],0,0)
        return ans