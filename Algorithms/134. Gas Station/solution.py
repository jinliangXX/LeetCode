class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        fu = 0
        start = 0
        remain = 0
        for i, num in enumerate(gas):
            remain += num - cost[i]
            if remain < 0:
                fu += remain
                remain = 0
                start = i + 1
        if remain + fu < 0:
            return -1
        else:
            return start
