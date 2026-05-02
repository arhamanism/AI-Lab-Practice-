from ortools.sat.python import cp_model
# Create model
model = cp_model.CpModel()
# 1. Creating Integer Variables
x = model.NewIntVar(0, 10, 'x') # x ∈ [0, 10]
y = model.NewIntVar(-5, 5, 'y') # y ∈ [-5, 5]
# 2. Creating Boolean Variables (Binary 0/1)
b1 = model.NewBoolVar('b1') # Boolean variable (0 or 1)
b2 = model.NewBoolVar('b2')
# 3. Creating Interval Variables (for scheduling problems)
start = model.NewIntVar(0, 10, 'start') # Start time
size = 5 # Fixed duration
interval = model.NewFixedSizeIntervalVar(start, size,
'interval_task')
# 4. Creating Optional Interval Variable (only valid if `b1` is 1)
optional_interval = model.NewOptionalFixedSizeIntervalVar(start,
size, b1, 'optional_task')
# Print created variables
print(f"Integer Variables: {x}, {y}")
print(f"Boolean Variables: {b1}, {b2}")
print(f"Interval Variable: {interval}")
print(f"Optional Interval Variable: {optional_interval}")