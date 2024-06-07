from typing import List


class Node:
    def __init__(self, letter) -> None:
        self.letter = letter
        self.isFinal = False
        self.nextNodes = {}


class Trie:
    def __init__(self) -> None:
        self.root = Node(None)

    def insert_word(self, word):
        cur = self.root
        for w in word:
            if not cur.nextNodes or not cur.nextNodes.get(w, None):
                cur.nextNodes[w] = Node(w)
            cur = cur.nextNodes[w]
        cur.isFinal = True

    def shortest_root_for(self, word):
        cur = self.root
        res = ""
        i = 0
        while not cur.isFinal and cur.nextNodes and i < len(word):
            res += word[i]
            cur = cur.nextNodes.get(word[i], None)
            if not cur:
                return word
            i += 1
        return res


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert_word(word)

        res = ""
        for word in sentence.split():
            res += trie.shortest_root_for(word) + " "
        return res[:-1]


assert (
    Solution().replaceWords(
        ["cat", "bat", "rat"], "the cattle was rattled by the battery"
    )
    == "the cat was rat by the bat"
)
assert (
    Solution().replaceWords(
        ["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    )
    == "a a a a a a a a bbb baba a"
)
