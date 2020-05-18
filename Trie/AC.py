"""
AC自动机
"""


class TreeNode:
    def __init__(self):
        self.fail = None
        self.count = 0  # 记录以该节点为结尾的字符串数目
        self.deep = 0   # 该节点距离根节点的距离
        self.children = [None] * 26  # 可以使用字典代替


class AC:
    def __init__(self):
        self.root = TreeNode()

    def build_ac(self, words):
        # 构建字典树
        for w in words:
            self.insert(w)

        # 建立fail索引
        p = self.root
        stack = []

        # 根节点的孩子节点的fail指向根节点
        for c in p.children:
            if c:
                c.fail = p
                stack.append(c)

        # 广度优先遍历得到每个节点的next节点
        while stack:
            p = stack.pop(0)

            for i in range(len(p.children)):
                c = p.children[i]
                f = p.fail

                if c:
                    while f:
                        if f.children[i]:
                            c.fail = f.children[i]
                            break
                        else:
                            f = f.fail
                    if not f:
                        c.fail = self.root
                    stack.append(c)

    def insert(self, str):
        p = self.root
        for c in str:
            index = ord(c) - ord('a')
            sub_node = p.children[index]
            if not sub_node:
                sub_node = TreeNode()
                sub_node.deep = p.deep + 1
                p.children[index] = sub_node  # 这步不能丢
            p = sub_node
        p.count += 1

    def search(self, str):
        res = {}
        cur = self.root

        for i in range(len(str)):
            s = str[i]
            index = ord(s) - ord("a")

            if not cur:
                cur = self.root

            while cur:
                c = cur.children[index]
                if c:
                    cur = c
                    if cur.count != 0:
                        start = i - cur.deep + 1
                        sub_str = str[start: i + 1]
                        if sub_str in res:
                            res[sub_str].append(start)
                        else:
                            res[sub_str] = [start]
                    if cur.fail.count != 0:
                        start = i - cur.fail.deep + 1
                        sub_str = str[start: i + 1]
                        if sub_str in res:
                            res[sub_str].append(start)
                        else:
                            res[sub_str] = [start]
                    break
                else:
                    cur = cur.fail

        return res


if __name__ == '__main__':
    words = ["abd", "abdk", "abchijn", "chnit", "ijabdf", "ijaij"]
    ac = AC()
    ac.build_ac(words)
    print(ac.search("abdchnijabdfk"))
