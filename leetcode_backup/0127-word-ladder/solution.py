from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    nxt = word[:i] + c + word[i + 1 :]
                    if nxt in wordSet:
                        wordSet.remove(nxt)
                        q.append((nxt, dist + 1))

        return 0
