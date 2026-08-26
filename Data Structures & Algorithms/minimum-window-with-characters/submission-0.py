class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq = {}
        for char in t:
            freq[char] = freq.get(char, 0) + 1
        
        window = {}
        best_len = float("inf")
        best_right = 0
        best_left = 0

        left = 0
        have = 0
        need = len(freq)

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in freq and window[char] == freq[char]:
                have += 1
            
            while have == need:
                current_len = right - left + 1
                if current_len < best_len:
                    best_len = current_len
                    best_left = left
                    best_right = right
                left_char = s[left]
                window[left_char] -= 1

                if left_char in freq and window[left_char] < freq[left_char]:
                    have -= 1
                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left:best_right+ 1]


        

