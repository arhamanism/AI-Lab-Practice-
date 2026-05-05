import math

class Node:
    def __init__(self, value = None):
        self.children = []
        self.minmax_val = None   # kept same name
        self.value = value

class MinMax_Agent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):   # FIXED: added self
        return "Goal Found!" if node.minmax_val is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)

        if goal_status == "Goal Found!":
            return f"MinMax value for the root node is {node.minmax_val}"
        else:
            return environment.compute_minmax(node, self.depth)

class environment: 
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []
    
    def getpercept(self, node):   # FIXED: added self
        return node
    
    def compute_minmax(self, node, depth, maximizing_player = True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value
        
        if maximizing_player:
            value = -math.inf

            for child in node.children:
                child_val = self.compute_minmax(child, depth-1, False)
                value = max(value, child_val)

            node.minmax_val = value
            self.computed_nodes.append(node.value)   # FIXED typo
            return value
        else:
            value = math.inf

            for child in node.children:
                child_val = self.compute_minmax(child, depth-1, True)
                value = min(child_val, value)

            node.minmax_val = value
            self.computed_nodes.append(node.value)
            return value
        
def run_agent(agent, environment, start_node):
    percept = environment.getpercept(start_node)
    result = agent.act(percept, environment)   # FIXED: capture result
    print(result)                              # FIXED: print it
    

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
environment1 = environment(root)

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