class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = {}
        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        
        left = 0
        right = 0
        window ={}

        while right < len(s2):
            char = s2[right]
            window[char] = window.get(char, 0) + 1
            # window has a fixed size i.e len(s1)
            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1
                #imp- no key's value should be 0
                if window[left_char] == 0:
                    del window[left_char]
                left += 1
            if freq == window:
                return True
            right += 1

        return False