class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build adjacency list: course -> list of next courses that depend on it
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def dfs(course):
            # if we are currently visiting this node, we found a cycle
            if state[course] == 1:
                return False
            # if already fully processed, no need to re-check
            if state[course] == 2:
                return True

            state[course] = 1  # mark as visiting
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            state[course] = 2  # mark as visited
            return True

        for c in range(numCourses):
            if state[c] == 0:
                if not dfs(c):
                    return False

        return True
