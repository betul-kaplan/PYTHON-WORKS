#Problem Statement
#Given a list of strings, group anagrams together.

#Example:

#Input:

#["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
#Note: All inputs will be in lowercase. The order of your output does not matter.

#Solution

strs = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]
anag = {}
for i in strs:
    element = "".join(sorted(i))
    if element in anag:
        anag[element].append(i)
    else:
        anag[element] = [i]
print(anag)
print(list(anag.values()))
