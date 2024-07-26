from collections import Counter, defaultdict
from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for str in strs:
        result["".join(sorted(str))].append(str)

    return list(result.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))