# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Problem Set 5
# Term:         Winter 2019


def vowel_extractor(chars):
    n_chars = ""
    for i in chars:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A"
 or i == "E" or i == "I" or i == "O" or i == "U"):
            n_chars = n_chars + i
    return n_chars


def translate_str(chars, old, new):
    n_str = ""
    for i in chars:
        if i == old:
            i = new    
        n_str = n_str + i    
    return n_str


def rotate_str(chars):
    new_chars = ""
    for i in chars:
        i = ord(i)
        if i >= ord("A") and i <= ord("Z") or i >= ord("a") and i <= ord("z"):
            i = i + 13
            if (chr(i - 13).islower() and i > ord("z")):
                i = i - 26
            elif (chr(i - 13).isupper() and i > ord("Z")):
                i = i - 26
        new_chars = new_chars + chr(i)
    return new_chars


def make_substr(chars, start, stop, step):
    substring = ""
    if stop > len(chars):
        stop = len(chars)
    for i in range(start, stop, step):
        substring = substring + chars[i]
    return substring


def longest_substr(s1, s2):
    start = 0
    stop = 0
    substr = ""
    longest = ""
    for i in range(len(s1)):
        for j in range(len(s2)):
            x = i
            if s1[i] == s2[j]:
                start = i
            while i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                i += 1
                j += 1
                stop = i
                substr = make_substr(s1, start, stop, 1)
                if len(longest) < len(substr):
                    longest = substr
            i = x
    return longest


def is_palindrome(word):
    back = ""
    words = ""
    for i in range(len(word)):
        if word[i] != " ":
            words = words + word[i]
    for i in range(len(words) - 1, -1, -1):
        back = back + words[i]
    return words == back
  

def word_initials(chars):
    first = True
    new_chars = ""
    for i in chars:
        if first and (ord(i) >= ord("A") and ord(i) <= ord("Z") or
 ord(i) >= ord("a") and ord(i) <= ord("z")):
            new_chars = new_chars + i
        if (ord(i) < ord("A") or (ord(i) > ord("Z") and ord(i) < ord("a"))
 or ord(i) > ord("z")):
            first = True
        else:
            first = False
    return new_chars
