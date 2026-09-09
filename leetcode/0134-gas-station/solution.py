class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas < total cost, impossible to complete circuit
        if sum(gas) < sum(cost):  # quick feasibility check
            return -1

        start = 0
        tank = 0
        n = len(gas)

        for i in range(n):
            tank += gas[i] - cost[i]
            # If we cannot reach station i+1 from current start
            if tank < 0:
                # Next station becomes new start, reset tank
                start = i + 1
                tank = 0

        return start
