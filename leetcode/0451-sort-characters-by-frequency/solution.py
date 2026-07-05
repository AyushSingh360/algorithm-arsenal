from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        # sort characters by frequency descending; tie order doesn't matter
        chars = sorted(cnt.items(), key=lambda kv: -kv[1])
        return "".join(ch * freq for ch, freq in chars)
