class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        size = len(candidates)

        def combination(cur_list, remain, start):
            if remain < 0:
                return
            if remain == 0:
                cur_list.sort()
                if cur_list not in res:
                    res.append(cur_list)
                return
            for i in range(start, size):
                cur_list.append(candidates[i])
                combination(cur_list[:], remain-candidates[i], i+1)
                cur_list.pop()
        combination([], target, 0)
        return res
