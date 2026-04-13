class Solution(object):
    def minWindow(self, s, t):
        from collections import Counter
        
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        window_count = {}
        
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            # Try to shrink window
            while have == need:
                # Update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # Remove left char
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""