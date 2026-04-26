class Solution:
    def sortVowels(self, s: str) -> str:
        li_s = list(s)
        dict_s = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for c in li_s:
            if c in vowels:
                dict_s[c] = dict_s.get(c, 0) + 1

        filtered_dict_s = {k: v for k, v in dict_s.items() if v != 0}
        sorted_dict_s = dict(sorted(filtered_dict_s.items(), key = lambda item: item[1], reverse = True))
        
        for idx in range(len(li_s)):
            if li_s[idx] in vowels:
                for vowel, q in sorted_dict_s.items():
                    if q != 0:
                        li_s[idx] = vowel
                        sorted_dict_s[vowel] -= 1
                        break
        
        return "".join(li_s)
        
