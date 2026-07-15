class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(s: str) -> bool:
            parts = s.split(".")
            if len(parts) != 4:
                return False
            for p in parts:
                # must be non-empty, all digits, length 1–3
                if not p or not p.isdigit() or len(p) > 3:
                    return False
                # no leading zeros unless the number is exactly "0"
                if len(p) > 1 and p[0] == "0":
                    return False
                # value range 0–255
                if not 0 <= int(p) <= 255:
                    return False
            return True

        def is_ipv6(s: str) -> bool:
            parts = s.split(":")
            if len(parts) != 8:
                return False
            hex_digits = "0123456789abcdefABCDEF"
            for p in parts:
                # length 1–4, non-empty
                if not (1 <= len(p) <= 4):
                    return False
                # all chars must be hex
                if not all(c in hex_digits for c in p):
                    return False
            return True

        if queryIP.count(".") > 0 and queryIP.count(":") == 0:
            return "IPv4" if is_ipv4(queryIP) else "Neither"
        if queryIP.count(":") > 0 and queryIP.count(".") == 0:
            return "IPv6" if is_ipv6(queryIP) else "Neither"
        return "Neither"
