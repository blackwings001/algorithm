# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def dfs(node):
            if not node:
                return None

            if node in lookup:
                return lookup[node]

            clone = Node(node.val, None, None)
            lookup[node] = clone

            clone.next = dfs(node.next)
            clone.random = dfs(node.random)

            return clone

        def bfs(node):
            if not node:
                return None

            clone = Node(node.val, None, None)
            lookup[node] = clone
            queue = [node]

            while queue:
                node = queue.pop(0)

                if node.next:
                    if node.next not in lookup:
                        queue.append(node.next)
                        lookup[node.next] = Node(node.next.val, None, None)
                    lookup[node].next = lookup[node.next]

                if node.random:
                    if node.random not in lookup:
                        queue.append(node.random)
                        lookup[node.random] = Node(node.random.val, None, None)
                    lookup[node].random = lookup[node.random]
            return clone

        lookup = {}
        # clone_node = dfs(head)
        clone_node = bfs(head)

        return clone_node


if __name__ == '__main__':
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node1.next = node2
    node1.random = node2
    node2.random = node2

    res = Solution().copyRandomList(node1)
    print(res)

