# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        def dfs(raw):
            if not raw:
                return None

            if raw in raw_table:
                return raw_table[raw]

            clone = Node(raw.val, [])
            raw_table[raw] = clone
            for i in raw.neighbors:
                clone.neighbors.append(dfs(i))

            return clone

        def bfs(raw):
            if not raw:
                return None

            clone = Node(raw.val, [])
            raw_table[raw] = clone

            from queue import Queue
            q = Queue()
            q.put(raw)

            while q.qsize() > 0:
                raw = q.get()
                for neighbor in raw.neighbors:
                    if neighbor not in raw_table:
                        neighbor_clone = Node(neighbor.val, [])
                        raw_table[neighbor] = neighbor_clone
                        q.put(neighbor)
                    raw_table[raw].neighbors.append(raw_table[neighbor])

            return clone

        raw_table = {}

        # clone_node = dfs(node)
        clone_node = bfs(node)
        return clone_node


if __name__ == '__main__':
    node1 = Node(1, [])
    node2 = Node(2, [])
    node3 = Node(3, [])
    node4 = Node(4, [])

    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node3)
    node2.neighbors.append(node1)
    node3.neighbors.append(node4)
    node3.neighbors.append(node2)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    res = Solution().cloneGraph(node1)
    print(res)



