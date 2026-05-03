"""
A logistics company is responsible for assigning delivery tasks to a fleet of vehicles. The company
has three vehicles: V1, V2, and V3—and five delivery locations labeled L1 through L5. Each
delivery location must be assigned to exactly one vehicle. However, the assignment must satisfy
several operational constraints. Each vehicle has a limited delivery capacity: V1 and V2 can handle
at most two deliveries each, while V3 can handle up to three deliveries. Additionally, certain
assignments are restricted: locations L1 and L2 cannot be assigned to the same vehicle, and
location L3 must be assigned specifically to vehicle V3.
To ensure fairness in workload distribution, the difference in the number of deliveries assigned to
V1 and V2 must not exceed one. Furthermore, there is a dependency constraint: if location L4 is
assigned to vehicle V1, then location L5 must also be assigned to V1. This problem can be modeled
as a Constraint Satisfaction Problem (CSP) where each location (l) is represented by a variable
(vehicle[l] in {V1, V2, V3}). Students are required to implement a function
solve_vehicle_assignment() using the OR-Tools CP-SAT solver. The solution should incorporate
counting constraints for vehicle capacities, logical implication constraints for dependencies, and
balancing constraints for workload distribution, and produce a valid assignment of locations to
vehicles as output.
"""

from ortools.sat.python import cp_model

model = cp_model.CpModel()

# Variables: each location -> vehicle (1=V1, 2=V2, 3=V3)
l1 = model.NewIntVar(1, 3, "l1")
l2 = model.NewIntVar(1, 3, "l2")
l3 = model.NewIntVar(1, 3, "l3")
l4 = model.NewIntVar(1, 3, "l4")
l5 = model.NewIntVar(1, 3, "l5")

locations = [l1, l2, l3, l4, l5]

# Constraint: L1 and L2 cannot be same vehicle
model.Add(l1 != l2)

# Constraint: L3 must be V3
model.Add(l3 == 3)

# Boolean: L4 is assigned to V1
l4_is_v1 = model.NewBoolVar("l4_is_v1")
model.Add(l4 == 1).OnlyEnforceIf(l4_is_v1)
model.Add(l4 != 1).OnlyEnforceIf(l4_is_v1.Not())

# Implication: if L4 is V1 → L5 must be V1
model.Add(l5 == 1).OnlyEnforceIf(l4_is_v1)

# Build assignment indicators
v1, v2, v3 = [], [], []

for i, loc in enumerate(locations):
    b1 = model.NewBoolVar(f"loc{i+1}_V1")
    b2 = model.NewBoolVar(f"loc{i+1}_V2")
    b3 = model.NewBoolVar(f"loc{i+1}_V3")

    model.Add(loc == 1).OnlyEnforceIf(b1)
    model.Add(loc != 1).OnlyEnforceIf(b1.Not())

    model.Add(loc == 2).OnlyEnforceIf(b2)
    model.Add(loc != 2).OnlyEnforceIf(b2.Not())

    model.Add(loc == 3).OnlyEnforceIf(b3)
    model.Add(loc != 3).OnlyEnforceIf(b3.Not())

    v1.append(b1)
    v2.append(b2)
    v3.append(b3)

v1_count = model.NewIntVar(0, 5, "v1_count")
v2_count = model.NewIntVar(0, 5, "v2_count")
v3_count = model.NewIntVar(0, 5, "v3_count")

model.Add(v1_count == sum(v1))
model.Add(v2_count == sum(v2))
model.Add(v3_count == sum(v3))

# Capacity constraints
model.Add(v1_count <= 2)
model.Add(v2_count <= 2)
model.Add(v3_count <= 3)

# Balance constraint: |V1 - V2| <= 1
diff = model.NewIntVar(0, 5, "diff")
model.AddAbsEquality(diff, v1_count - v2_count)
model.Add(diff <= 1)

# Solver
solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True


class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, vars):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.vars = vars
        self.count = 0

    def OnSolutionCallback(self):
        self.count += 1
        print(f"\nSolution {self.count}")
        for i, var in enumerate(self.vars):
            print(f"L{i+1}: V{self.Value(var)}")


printer = SolutionPrinter([l1, l2, l3, l4, l5])
solver.SearchForAllSolutions(model, printer)

print("\nTotal solutions:", printer.count)