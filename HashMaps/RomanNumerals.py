class Solution:
    romanNumerals = {}
    romanNumerals["I"] = 1
    romanNumerals["V"] = 5
    romanNumerals["X"] = 10
    romanNumerals["L"] = 50
    romanNumerals["C"] = 100
    romanNumerals["D"] = 500
    romanNumerals["M"] = 1000
    def romanToInt(self, s: str) -> int:
        total = 0
        i=0
        while i < (len(s)):
                if (i) == len(s)-1:
                    total+=self.romanNumerals[s[i]]
                    i+=1
                elif self.romanNumerals[s[i]] < self.romanNumerals[s[i+1]]:
                    difference = self.romanNumerals[s[i+1]]- self.romanNumerals[s[i]]
                    i+=2
                    total+=difference
                else:
                    total+=self.romanNumerals[s[i]]
                    i+=1
           
            
        return total



        