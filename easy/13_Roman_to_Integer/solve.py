# my solve - 45ms
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {"M": 1000, "D": 500, "C": 100,
                  "L": 50, "X": 10, "V": 5, "I": 1}
        check = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
        check_keys = list(check.keys())
        result = 0
        for ind, s_ in enumerate(s):
            if ind != len(s)-1 and s_ in check_keys and s[ind+1] in check[s_]:
                result -= symbol[s_]
            else:
                result += symbol[s_]
        return result


# 인터넷 최단시간 코드
symbolToIntDict = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}


class Solution_internet:
    def romanToInt(self, s: str) -> int:
        prevValue = symbolToIntDict["M"]
        totalValue = 0
        for c in s:
            currentValue = symbolToIntDict[c]
            if prevValue < currentValue:
                totalValue -= prevValue * 2
            totalValue += currentValue
            prevValue = currentValue
        return totalValue


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
