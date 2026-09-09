from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        n = len(data)

        while i < n:
            byte = data[i] & 0xFF  # only use least significant 8 bits

            # Determine number of bytes for current UTF-8 character
            if byte & 0x80 == 0:  # 0xxxxxxx -> 1-byte
                num_bytes = 1
            elif byte & 0xE0 == 0xC0:  # 110xxxxx -> 2-byte
                num_bytes = 2
            elif byte & 0xF0 == 0xE0:  # 1110xxxx -> 3-byte
                num_bytes = 3
            elif byte & 0xF8 == 0xF0:  # 11110xxx -> 4-byte
                num_bytes = 4
            else:
                # Invalid leading byte pattern
                return False

            # Not enough bytes left for this character
            if i + num_bytes > n:
                return False

            # Check continuation bytes: must start with 10xxxxxx
            for j in range(1, num_bytes):
                if data[i + j] & 0xC0 != 0x80:
                    return False

            i += num_bytes

        return True
