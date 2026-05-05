import math

class Node:
    def __init__(self, value):
        self.value = value
        self.minmax_val = None
        self.children = []

class MinMax_Agent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal Found" if node.minmax_val is not None else "Searching"
    
    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal Found":
            return f"Minimax value of Node is:{node.minmax_val}"
        else:
            return environment.alphabetaSearch(node, self.depth, -math.inf, math.inf, True)
    
class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []
    
    def getpercept(self, node):
        return node
    
    def alphabetaSearch(self, node, depth, alpha, beta, maximizing_player=True):
       pass



def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)

root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0)
n12 = Node(1)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

# define depth for Minimax
depth = 3
agent = MinMax_Agent(depth)
environment1 = Environment(root)

run_agent(agent, environment1, root)

print("Computed Nodes:", environment1.computed_nodes)
print("Minimax values: ")
print("A: ", root.minmax_val)   # FIXED name
print("B: ", n1.minmax_val)
print("C: ", n2.minmax_val)
print("D: ", n3.minmax_val)
print("E: ", n4.minmax_val)
print("F: ", n5.minmax_val)
print("G: ", n6.minmax_val)