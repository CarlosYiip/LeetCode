class Solution(object):
    def numWays(self, n, k):
        if not n:
            return 0
        prev = (k, 0)
        for i in range(n-1):
            prev_total_ways = prev[0]
            prev_duplicates = prev[1]
            this_total_ways = (prev_total_ways - prev_duplicates) * k + prev_duplicates * (k - 1)
            this_duplicates = prev_total_ways - prev_duplicates
            prev = (this_total_ways, this_duplicates)
        return prev[0]
