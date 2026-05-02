"""
A delivery company must assign time slots to four deliveries: D1, D2, D3, and D4. The available
time slots are Morning (1), Afternoon (2), and Evening (3). Each delivery must be assigned exactly
one-time slot from the given options. However, certain constraints must be satisfied while
assigning these slots. Delivery D1 and D2 cannot be scheduled at the same time, meaning their
assigned slots must be different. Delivery D3 must be scheduled before D4, so the time slot
assigned to D3 must be less than that of D4. Additionally, D2 cannot be assigned to the Morning
slot (1). Students are required to model this problem as a Constraint Satisfaction Problem (CSP)
by defining appropriate variables for each delivery, specifying the domain of possible time slots
for each variable, and formally expressing all constraints using mathematical or logical notation,
including inequality and ordering constraints.
"""

from ortools.sat.python import cp_model

model = cp_model.CpModel()

name_map = {
    "Morning": 1,
    "Afternoon": 2,
    "Evening": 3
}

D1 = model.new_int_var(1,3 ,"D1")
D2 = model.new_int_var(1,3 ,"D2")
D3 = model.new_int_var(1,3 ,"D3")
D4 = model.new_int_var(1,3 ,"D4")

model.add(D1 != D2)
model.add(D4 > D3)
model.add(D2 != 1)

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self,D1,D2,D3,D4):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.D1 = D1
        self.D2 = D2
        self.D3 = D3
        self.D4 = D4
        self.count = 0
    
    def OnSolutionCallback(self):
        self.count += 1
        print(f"\nSolution {self.count}:")
        print("D1: ",self.value(self.D1))
        print("D2: ",self.value(self.D2))
        print("D3: ",self.value(self.D3))
        print("D4: ",self.value(self.D4))

solution_printer = SolutionPrinter(D1, D2, D3, D4)
solver.SearchForAllSolutions(model, solution_printer)

print("\nTotal solutions found:", solution_printer.count)



