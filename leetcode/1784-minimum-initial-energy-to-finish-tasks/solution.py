class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by (minimum - actual) in descending order
        # Tasks with higher "savings" should be done first
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        current_energy = 0
        initial_energy = 0

        for actual, minimum in tasks:
            # If we don't have enough energy to start this task
            if current_energy < minimum:
                needed = minimum - current_energy
                initial_energy += needed
                current_energy += needed

            # Complete the task (consume actual energy)
            current_energy -= actual

        return initial_energy
