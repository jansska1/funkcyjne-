def check_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

anagram_check = check_anagrams("listen", "silent")
print("Are anagrams:", anagram_check)
