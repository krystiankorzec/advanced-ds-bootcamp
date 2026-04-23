# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    left = 0
    right = len(s) -1  
    while right > left:
        while right > left and not s[right].isalnum():
            right -= 1
        while right > left and not s[left].isalnum():
            left += 1
        if s[right].lower() != s[left].lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    assert isPalindrome(s) is True
    s = " "
    assert isPalindrome(s) is True
    s = "race a car"
    assert isPalindrome(s) is False
    print("Tests passed")




s = "racecar"
t = "carrace"
counts = {}
for letter in s:
    counts[letter] = counts.get(letter, 0) + 1
for letter in t:
    if letter not in counts:
        print(False)
    counts[letter] -= 1
    if counts[letter] < 0:
        print(False)
    