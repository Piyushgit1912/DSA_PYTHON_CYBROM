# # Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution(object):
    def isPalindrome(self, str):
        """
        :type s: str
        :rtype: bool
        """
        res=""
        str=str.lower()
        for i in str:
         if i.isalnum():
            res+=i
        if res==res[::-1]:
            return True
        else:
            return False