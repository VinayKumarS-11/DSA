class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s = input("Enter a string: ")

obj = Solution()
print(obj.reverseWords(s))