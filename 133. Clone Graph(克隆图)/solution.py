# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        self.nodes = dict()

        def get_result(node: Node):
            if not node:
                return None
            if node.val in self.nodes:
                return self.nodes[node.val]
            new_node = Node(node.val)
            new_node.neighbors = list()
            self.nodes[node.val] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(get_result(neighbor))
            return new_node

        get_result(node)
        return self.nodes[node.val]
