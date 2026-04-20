#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s, t):
    counts = {}
    for letter in s:
        counts[letter] = counts.get(letter, 0) + 1
    for letter in t:
        if letter not in counts:
            return False
        counts[letter] += -1
        if counts[letter] < 0:
            return False
    return True

if __name__ == "__main__":
    s = "rat"
    t = "car"   
    assert isAnagram(s,t) is False
    s = "anagram"
    t = "anargam"
    assert isAnagram(s,t) is True
    print("Tests passed!")
