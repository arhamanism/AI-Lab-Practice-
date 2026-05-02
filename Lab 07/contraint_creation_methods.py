from ortools.sat.python import cp_model
# Create model
model = cp_model.CpModel()
# Define variables
x = model.NewIntVar(0, 10, "x")
y = model.NewIntVar(0, 10, "y")
z = model.NewIntVar(0, 10, "z")

# Applying constraints
model.Add(x + y <= 10)
model.AddAllDifferent([x, y, z])
# Allowed combinations for x,y
model.AddAllowedAssignments([x, y], [(1, 2), (3, 4)])
# Forbidden combinations
model.AddForbiddenAssignments([x, y], [(1, 1), (2, 2)])
# Min and Max targets (separate variables)
min_target = model.NewIntVar(0, 10, "min_target")
max_target = model.NewIntVar(0, 10, "max_target")
model.AddMinEquality(min_target, [x, y, z])
model.AddMaxEquality(max_target, [x, y, z])
# Division constraint
num = model.NewIntVar(1, 10, "num")
denom = model.NewIntVar(1, 5, "denom")
div_target = model.NewIntVar(0, 10, "div_target")
model.AddDivisionEquality(div_target, num, denom)
# Multiplication constraint
factors = [model.NewIntVar(1, 5, f"f{i}") for i in range(2)]
prod_target = model.NewIntVar(1, 25, "prod_target")
model.AddMultiplicationEquality(prod_target, factors)
# Solver
solver = cp_model.CpSolver()
status = solver.Solve(model)
# Output results if feasible
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solution Found\n")
    print("x =", solver.Value(x))
    print("y =", solver.Value(y))
    print("z =", solver.Value(z))
    print("\nMinimum value =", solver.Value(min_target))
    print("Maximum value =", solver.Value(max_target))
    print("\nDivision result =", solver.Value(div_target))
    print("Numerator =", solver.Value(num))|
    print("Denominator =", solver.Value(denom))
    print("\nProduct result =", solver.Value(prod_target))
    print("Factors =", [solver.Value(f) for f in factors])
else:
    print("No feasible solution found.")