'''
    1768. Merge Strings Alternately

    Algorithm with pseudocode
    -------------------------
    1.	max_len: int = ma_len(word1, word2)
    2.	for range(max_len)
    3.	Initially output_str = ""
    4.	if word1[i] is not None -> output_str += word1[i]
    5.	if word2[i] is not None -> output_str += word2[i]
    6.	finally return output_str
'''

class Solution_01:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len: int = int(max(len(word1), len(word2)))
        output_str = ""
        for i in range(max_len):
            if i < len(word1):
                output_str += word1[i]
            if i < len(word2):
                output_str += word2[i]
        return output_str
    

if __name__ == '__main__':
    word1, word2 = input(), input()
    obj = Solution_01()
    print(obj.mergeAlternately(word1, word2))