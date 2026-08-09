class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while (i< len(s)):
            j = s.find("#", i)
            length = int(s[i:j])

            start = j + 1
            end = start + length

            result.append(s[start:end])

            i = end
        
        return result