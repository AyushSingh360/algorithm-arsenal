from typing import Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            # Walk the pattern from position index starting at node
            for i in range(index, len(word)):
                ch = word[i]
                if ch == ".":
                    # Try all possible children for wildcard
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if ch not in node.children:
                        return False
                    node = node.children[ch]
            return node.is_end

        return dfs(0, self.root)
