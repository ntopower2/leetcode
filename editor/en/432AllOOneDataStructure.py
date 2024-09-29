#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start


class Node:
    def __init__(self, word, next=None, prev=None, val=1) -> None:
        self.words = set([word])
        self.next = next
        if next:
            next.prev = self
        self.prev = prev
        if prev:
            prev.next = self
        self.value = val


class AllOne:

    def __init__(self):
        self.words = {}
        self.start = None
        self.end = None

    def inc(self, key: str) -> None:
        if not self.start:
            node = Node(key)
            self.start = self.end = node
            self.words[key] = node
            return

        if key not in self.words:
            if self.start.value == 1:
                self.start.words.add(key)
            else:
                node = Node(key, self.start)
                self.start.prev = node
                self.start = node
            self.words[key] = self.start
            return

        tmp = self.words[key]
        if not tmp.next or tmp.value + 1 != tmp.next.value:
            node = Node(key, tmp.next, tmp, tmp.value + 1)
            tmp.next = node
            if not node.next:
                self.end = node
            self.words[key] = node
        else:
            node = tmp.next
            node.words.add(key)
            self.words[key] = node

        tmp.words.remove(key)
        if not len(tmp.words):
            node.prev = tmp.prev
            if not tmp.prev:
                self.start = node
            else:
                tmp.prev.next = node

    def dec(self, key: str) -> None:
        tmp = self.words[key]
        if tmp.value == 1:
            if len(tmp.words) == 1:
                if tmp.next:
                    self.start = tmp.next
                    tmp.next.prev = None
                else:
                    self.start = None
                    self.end = None
            else:
                tmp.words.remove(key)
            self.words.pop(key)
        elif not tmp.prev or tmp.prev.value != tmp.value - 1:
            tmp.words.remove(key)
            if tmp.words:
                node = Node(key, tmp, val=tmp.value - 1)
            else:
                node = Node(key, tmp.next, val=tmp.value - 1)
                if not tmp.next:
                    self.end = node

            if tmp.prev:
                node.prev = tmp.prev
                tmp.prev.next = node
            else:
                self.start = node
            self.words[key] = node
            tmp.prev = node
        else:
            tmp.words.remove(key)
            if not len(tmp.words):
                tmp.prev.next = tmp.next
                if tmp.next:
                    tmp.next.prev = tmp.prev
                else:
                    self.end = tmp.prev
            tmp.prev.words.add(key)
            self.words[key] = tmp.prev

    def getMaxKey(self) -> str:
        return "" if not self.end else next(iter(self.end.words))

    def getMinKey(self) -> str:
        return "" if not self.start else next(iter(self.start.words))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end
def driver(operations, values):
    struct = None  # This will hold the deque instance
    results = []  # List to store the results of each operation

    for i, operation in enumerate(operations):
        if operation == "AllOne":
            struct = AllOne()
            results.append(None)
        elif operation == "inc":
            struct.inc(values[i][0])
            results.append(None)

        elif operation == "dec":
            struct.dec(values[i][0])
            results.append(None)

        elif operation == "getMaxKey":
            results.append(struct.getMaxKey())

        elif operation == "getMinKey":
            results.append(struct.getMinKey())

    return results


assert driver(
    [
        "AllOne",
        "inc",
        "inc",
        "inc",
        "inc",
        "inc",
        "inc",
        "inc",
        "inc",
        "inc",
        "inc",
        "inc",
        "inc",
        "getMinKey",
    ],
    [
        [],
        ["a"],
        ["b"],
        ["c"],
        ["d"],
        ["a"],
        ["b"],
        ["c"],
        ["d"],
        ["c"],
        ["d"],
        ["d"],
        ["a"],
        [],
    ],
) == [None, None, None, None, None, None, None, None, None, None, None, None, None, "b"]
