from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # 1) BFS to compute distance (level) from beginWord and build parent list
        dist = {beginWord: 0}
        parents = defaultdict(list)  # child -> list of parents
        q = deque([beginWord])
        found_end = False
        level = 0

        while q and not found_end:
            level += 1
            for _ in range(len(q)):
                word = q.popleft()
                for nei in self._neighbors(word, word_set):
                    if nei not in dist:  # first time seen: shortest distance
                        dist[nei] = level
                        parents[nei].append(word)
                        if nei == endWord:
                            found_end = True
                        else:
                            q.append(nei)
                    elif dist[nei] == level:  # another shortest parent
                        parents[nei].append(word)

        if endWord not in dist:
            return []

        # 2) DFS/backtrack from endWord to beginWord using parents map
        res = []
        path = [endWord]

        def dfs(word: str):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return res

    def _neighbors(self, word: str, word_set: set) -> List[str]:
        res = []
        chars = list(word)
        for i in range(len(chars)):
            original = chars[i]
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == original:
                    continue
                chars[i] = c
                new_word = "".join(chars)
                if new_word in word_set:
                    res.append(new_word)
            chars[i] = original
        return res
