#Write a function that checks if a given word is a palindrome. Character case should be ignored.


def checkPalindrome(s):
    return s.lower() == s[::-1].lower()
 
name = "nitIN"
ispalindeome = checkPalindrome(name)
 
if ispalindeome:
    print("Yes")
else:
    print("No")