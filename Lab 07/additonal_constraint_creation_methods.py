from ortools.sat.python import cp_model
model = cp_model.CpModel()

# ─── 1. DEFINE YOUR ENTITIES AND DOMAIN ───────────────────────────────────────

entities = ['A', 'B', 'C', 'D']   # replace with your variables (students, courses, etc.)
domain_min = 1
domain_max = 4  # replace with your domain size

# Single variable per entity  (use this when each entity gets ONE assignment)
s = {e: model.NewIntVar(domain_min, domain_max, e) for e in entities}

# Multiple variables per entity  (use this when each entity needs TWO assignments, e.g. timeslot + room)

# timeslot = {e: model.NewIntVar(1, 4, f'ts_{e}') for e in entities}
# room     = {e: model.NewIntVar(1, 3, f'rm_{e}') for e in entities}
  
# ─── 2. CONSTRAINTS ───────────────────────────────────────────────────────────

# --- All different (no two entities share the same value) ---
model.AddAllDifferent(s.values())

# --- Direct equality / inequality ---
model.Add(s['A'] != s['B'])          # A and B must differ
model.Add(s['A'] == s['B'])          # A and B must be equal

# --- Ordering ---
model.Add(s['A'] < s['B'])           # A must come before B
model.Add(s['A'] <= s['B'])

# --- Fixed value / forbidden value ---
model.Add(s['A'] == 2)               # A must be assigned value 2
model.Add(s['A'] != 1)               # A cannot be value 1

# --- Domain restriction (pick subset of values) ---
model.AddLinearConstraint(s['A'], 3, 4)   # A must be 3 or 4  (lower ≤ var ≤ upper)

# --- Even / odd ---
model.AddModuloEquality(0, s['A'], 2)     # A must be even
# model.AddModuloEquality(1, s['A'], 2)   # A must be odd

# --- Must be adjacent (|A - B| == 1) ---
diff_ab = model.NewIntVar(-domain_max, domain_max, 'diff_ab')
model.Add(diff_ab == s['A'] - s['B'])
model.AddAbsEquality(1, diff_ab)

# --- Must NOT be adjacent (|A - B| != 1) ---
diff_cd = model.NewIntVar(-domain_max, domain_max, 'diff_cd')
abs_cd  = model.NewIntVar(0, domain_max, 'abs_cd')
model.Add(diff_cd == s['C'] - s['D'])
model.AddAbsEquality(abs_cd, diff_cd)
model.Add(abs_cd != 1)

# --- Conflict: two entities cannot share the same value (same as !=) ---
model.Add(s['B'] != s['C'])

# --- Two entities share the same room but different timeslot (multi-variable) ---
# model.Add(room['A'] != room['B'])         # different rooms
# b_same_room = model.NewBoolVar('same_rm_AB')
# model.Add(room['A'] == room['B']).OnlyEnforceIf(b_same_room)
# model.Add(timeslot['A'] != timeslot['B']).OnlyEnforceIf(b_same_room)

# --- Capacity constraint (multi-variable, room must fit enrollment) ---
# enrollments = {'A': 35, 'B': 50, 'C': 45}
# capacities  = {1: 40, 2: 60, 3: 100}         # room_id -> capacity
# for e in entities:
#     for room_id, cap in capacities.items():
#         b = model.NewBoolVar(f'{e}_in_r{room_id}')
#         model.Add(room[e] == room_id).OnlyEnforceIf(b)
#         model.Add(room[e] != room_id).OnlyEnforceIf(b.Not())
#         if enrollments[e] > cap:
#             model.Add(b == 0)                  # enrollment exceeds capacity → forbidden

# ─── 3. SOLVE ─────────────────────────────────────────────────────────────────

solver = cp_model.CpSolver()
status = solver.Solve(model)

# ─── 4. OUTPUT ────────────────────────────────────────────────────────────────

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solution:")
    results = sorted([(e, solver.Value(var)) for e, var in s.items()], key=lambda x: x[1])
    for entity, value in results:
        print(f"  {entity}: {value}")

    # For multi-variable output:
    # for e in entities:
    #     print(f"  {e}: slot={solver.Value(timeslot[e])}  room=R{solver.Value(room[e])}")
else:
    print("No solution found.")
```