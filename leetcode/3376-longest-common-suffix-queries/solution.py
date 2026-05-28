from typing import List


class TrieNode:
    __slots__ = ("children", "best_idx", "best_len")

    def __init__(self):
        self.children = [-1] * 26
        self.best_idx = -1
        self.best_len = 10**18


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        def better(i: int, j: int) -> bool:
            return (
                j == -1
                or len(wordsContainer[i]) < len(wordsContainer[j])
                or (len(wordsContainer[i]) == len(wordsContainer[j]) and i < j)
            )

        trie = [TrieNode()]

        def update(node_idx: int, word_idx: int):
            node = trie[node_idx]
            if better(word_idx, node.best_idx):
                node.best_idx = word_idx
                node.best_len = len(wordsContainer[word_idx])

        for i, w in enumerate(wordsContainer):
            node_idx = 0
            update(node_idx, i)
            for ch in reversed(w):
                c = ord(ch) - 97
                if trie[node_idx].children[c] == -1:
                    trie[node_idx].children[c] = len(trie)
                    trie.append(TrieNode())
                node_idx = trie[node_idx].children[c]
                update(node_idx, i)

        ans = []
        for q in wordsQuery:
            node_idx = 0
            best = trie[0].best_idx
            for ch in reversed(q):
                c = ord(ch) - 97
                nxt = trie[node_idx].children[c]
                if nxt == -1:
                    break
                node_idx = nxt
                best = trie[node_idx].best_idx
            ans.append(best)
        return ans
