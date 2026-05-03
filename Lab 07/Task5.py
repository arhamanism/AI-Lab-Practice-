"""
A university needs to schedule final exams for five subjects: Math, Physics, AI, Operating Systems
(OS), and Databases (DB). The exams are to be conducted over three days, with each day
consisting of two available time slots, resulting in a total of six slots labeled from 1 to 6. Each
subject must be assigned exactly one of these time slots. However, the scheduling must satisfy
several constraints. Certain subjects share common students and therefore cannot be scheduled at
the same time; specifically, Math cannot be scheduled with Physics, AI cannot be scheduled with
OS, and OS cannot be scheduled with DB.
Additionally, no more than two exams can be scheduled on the same day. The slots are grouped
into days as follows: Day 1 includes slots 1 and 2, Day 2 includes slots 3 and 4, and Day 3 includes
slots 5 and 6. Students also require sufficient rest between certain exams; therefore, there must be
a minimum gap of at least two slots between AI and OS. Furthermore, there is a strict ordering
constraint such that the Math exam must be scheduled before the DB exam. To manage resource
limitations, each slot can accommodate at most two exams.
This problem can be modeled as a Constraint Satisfaction Problem (CSP) where each subject (s)
is represented by a variable (exam[s] in {1,2,3,4,5,6}). Students are required to implement a
function solve_exam_schedule() using the OR-Tools CP-SAT solver. The implementation should
define variables, enforce all constraints including conflict, spacing, ordering, and capacity
constraints, and output a valid exam schedule assigning a slot to each subject.
"""
from ortools.sat.python import cp_model


def solve_exam_schedule():
    model = cp_model.CpModel()

    # -------------------------
    # 1. VARIABLES
    # -------------------------
    subjects = ["Math", "Physics", "AI", "OS", "DB"]

    exam = {
        s: model.NewIntVar(1, 6, s) for s in subjects
    }

    Math = exam["Math"]
    Physics = exam["Physics"]
    AI = exam["AI"]
    OS = exam["OS"]
    DB = exam["DB"]

    # -------------------------
    # 2. CONFLICT CONSTRAINTS
    # -------------------------
    model.Add(Math != Physics)
    model.Add(AI != OS)
    model.Add(OS != DB)

    # -------------------------
    # 3. ORDERING CONSTRAINT
    # -------------------------
    model.Add(Math < DB)

    # -------------------------
    # 4. GAP CONSTRAINT (AI & OS)
    # -------------------------
    diff = model.NewIntVar(0, 6, "diff")
    model.AddAbsEquality(diff, AI - OS)
    model.Add(diff >= 2)

    # -------------------------
    # 5. SLOT CAPACITY CONSTRAINT
    # (max 2 exams per slot)
    # -------------------------
    slots = range(1, 7)

    slot_counts = []

    for s in slots:
        b_vars = []

        for subj in subjects:
            b = model.NewBoolVar(f"{subj}_in_{s}")

            model.Add(exam[subj] == s).OnlyEnforceIf(b)
            model.Add(exam[subj] != s).OnlyEnforceIf(b.Not())

            b_vars.append(b)

        count = model.NewIntVar(0, 5, f"count_slot_{s}")
        model.Add(count == sum(b_vars))

        model.Add(count <= 2)

        slot_counts.append(count)

    # -------------------------
    # 6. DAY CONSTRAINTS
    # -------------------------
    # Day 1: slots 1,2
    # Day 2: slots 3,4
    # Day 3: slots 5,6

    def day_constraint(slot_list):
        b_vars = []

        for subj in subjects:
            for s in slot_list:
                b = model.NewBoolVar(f"{subj}_in_day_{slot_list}_{s}")

                model.Add(exam[subj] == s).OnlyEnforceIf(b)
                model.Add(exam[subj] != s).OnlyEnforceIf(b.Not())

                b_vars.append(b)

        count = model.NewIntVar(0, 5, "day_count")
        model.Add(count == sum(b_vars))

        model.Add(count <= 2)

    day_constraint([1, 2])
    day_constraint([3, 4])
    day_constraint([5, 6])

    # -------------------------
    # 7. SOLVER
    # -------------------------
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = True

    # -------------------------
    # 8. PRINT SOLUTIONS
    # -------------------------
    class Printer(cp_model.CpSolverSolutionCallback):
        def __init__(self, exam_vars):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.exam_vars = exam_vars
            self.count = 0

        def OnSolutionCallback(self):
            self.count += 1
            print(f"\nSolution {self.count}")
            for s in subjects:
                print(f"{s}: Slot {self.Value(exam[s])}")

    printer = Printer(exam)

    solver.SearchForAllSolutions(model, printer)

    print("\nTotal solutions:", printer.count)


# Run it
solve_exam_schedule()
