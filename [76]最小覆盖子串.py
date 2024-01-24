# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        need_char_2_count = {}
        for char in t:
            if char not in need_char_2_count:
                need_char_2_count[char] = 1
            else:
                need_char_2_count[char] += 1
        
        left, right = 0, 0
        window_char_2_count = {}
        valid = 0
        
        window_left, window_len = 0, math.inf
        while right < len(s):
            
            # 更新窗口内的数据分布
            if s[right] in window_char_2_count:
                window_char_2_count[s[right]] += 1
            else:
                window_char_2_count[s[right]] = 1
            
            if s[right] in need_char_2_count and \
                    window_char_2_count[s[right]] == need_char_2_count[s[right]]:
                valid += 1
            
            right += 1
            while valid == len(need_char_2_count):
                if right - left < window_len:
                    window_len = right - left
                    window_left = left
                
                # 更新窗口内的数据分布
                if s[left] in need_char_2_count and \
                        window_char_2_count[s[left]] == need_char_2_count[s[left]]:
                    valid -= 1
                
                window_char_2_count[s[left]] -= 1
                left += 1
        
        if window_len == math.inf:
            return ""
        else:
            return s[window_left:window_left + window_len]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
    print(solution.minWindow("aa", "aa"), "aa")
    print(solution.minWindow("a", "a"), "a")
    print(solution.minWindow("a", "aa"), "")
