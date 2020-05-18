"""
Trie树
"""


class TreeNode:
    def __init__(self):
        self.count = 0
        self.children = [None] * 26


class Tree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, str):
        p = self.root
        for c in str:
            index = ord(c) - ord('a')
            sub_node = p.children[index]
            if not sub_node:
                sub_node = TreeNode()
                p.children[index] = sub_node  # 这步不能丢
            p = sub_node
        p.count += 1

    def search(self, str):
        p = self.root
        for c in str:
            index = ord(c) - ord("a")
            sub_node = p.children[index]
            if not sub_node:
                return -1
            p = sub_node
        return p.count


if __name__ == '__main__':
    trie_tree = Tree()
    trie_tree.insert("joe")
    trie_tree.insert("john")
    trie_tree.insert("johnny")
    trie_tree.insert("jane")
    trie_tree.insert("jane")
    trie_tree.insert("jack")
    print(trie_tree.search("jane"))
    print(trie_tree.search("hello"))
