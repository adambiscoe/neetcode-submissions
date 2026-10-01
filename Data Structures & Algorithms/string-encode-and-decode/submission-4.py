class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []

        for string in strs:
            encoded.append(str(len(string)))
            encoded.append("#")
            encoded.append(string)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Find the separator after the length
            j = s.index("#", i)

            # Parse the string length
            length = int(s[i:j])

            # Move past "length#"
            i = j + 1

            # Read exactly `length` characters
            decoded.append(s[i:i + length])

            # Move to the next encoded string
            i += length

        return decoded