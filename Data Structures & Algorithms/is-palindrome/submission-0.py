class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleanup text and lowercase it.
        cleaned = "".join(char for char in s if char.isalnum()).lower()
        # pointer at start of str
        for i in range(len(cleaned) // 2):
            # end of str
            j = len(cleaned) - 1 - i
            if cleaned[i] != cleaned[j]:
                return False
        return True