# =========================
# 1. IMPORT LIBRARY
# =========================
from ortools.sat.python import cp_model

# =========================
# 2. CREATE MODEL
# =========================
model = cp_model.CpModel()

# =========================
# 3. DEFINE VARIABLES
# =========================
x = model.NewIntVar(0, 10, "x")
y = model.NewIntVar(0, 10, "y")
z = model.NewIntVar(0, 10, "z")

# =========================
# 4. DEFINE CONSTRAINTS
# =========================
model.Add(x + y <= 10)
model.Add(x != y)
model.AddAllDifferent([x, y, z])

# =========================
# 5. CREATE SOLVER
# =========================
solver = cp_model.CpSolver()

# =========================
# 6. FIND ALL SOLUTIONS (FIXED)
# =========================
solver.parameters.enumerate_all_solutions = True

# 🔹 ADD CALLBACK CLASS
class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, x, y, z):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.x = x
        self.y = y
        self.z = z
        self.count = 0

    def OnSolutionCallback(self):
        self.count += 1
        print(f"\nSolution {self.count}:")
        print("x =", self.Value(self.x))
        print("y =", self.Value(self.y))
        print("z =", self.Value(self.z))

# =========================
# 7. SOLVE MODEL (FIXED)
# =========================
solution_printer = SolutionPrinter(x, y, z)
solver.SearchForAllSolutions(model, solution_printer)

# =========================
# 8. PRINT TOTAL SOLUTIONS
# =========================
print("\nTotal solutions found:", solution_printer.count)