class Solution(object):
    def isAnagram(self, s, t):
        return str(list(s).sort()) == str(list(t).sort())
        