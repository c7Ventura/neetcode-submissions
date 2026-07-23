class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleanup text and lowercase it.
        s = "".join(char for char in s if char.isalnum()).lower()
        # pointer at start of str
        for i in range(len(s) // 2):
            # end of str
            j = len(s) - 1 - i
            if s[i] != s[j]:
                return False
        return True