"""
A university needs to schedule six courses: CS101, CS102, AI201, DS202, SE301, and ML401—
into a limited number of time slots and rooms. There are four available time slots, represented as
{1, 2, 3, 4}, and three rooms: R1 with a capacity of 40 students, R2 with a capacity of 60 students,
and R3 with a capacity of 100 students. Each course has a specific number of enrolled students:
CS101 has 35 students, CS102 has 50, AI201 has 45, DS202 has 60, SE301 has 30, and ML401
has 80. Some courses have overlapping student enrollments, meaning they cannot be scheduled at
the same time. Specifically, CS101 conflicts with CS102, CS102 conflicts with AI201, AI201
conflicts with ML401, and DS202 conflicts with SE301.
To model this as a Constraint Satisfaction Problem (CSP), each course must be assigned both a
time slot and a room. Therefore, for each course (c), two variables are defined: (timeslot[c] in
{1,2,3,4}) and (room[c] in {R1, R2, R3}). The assignment must satisfy several constraints. First,
conflicting courses must not be scheduled in the same time slot. Second, the assigned room for
each course must have sufficient capacity to accommodate all enrolled students. Third, no two
courses can be scheduled in the same room at the same time. Additionally, ML401 must be
scheduled in one of the last two time slots (3 or 4), while DS202 must be scheduled in one of the
morning slots (1 or 2).

Students are required to implement a function solve_course_timetabling() using the OR-Tools CP-
SAT solver, where they will define the variables, encode all constraints, and compute a feasible

timetable. The output should display the assigned time slot and room for each course in a clear
format.
"""

from ortools.sat.python import cp_model

model = cp_model.CpModel()

room_seat_map = {
    "R1": 40,
    "R2": 60,
    "R3": 100
}

num_of_students_enrolled_in_course_map = {
    "CS101": 35,
    "CS102": 50,
    "AI201": 45,
    "DS202": 60,
    "SE301": 30,
    "ML401": 80
}

# =========================
# VARIABLES
# =========================
CS101_time_slot = model.NewIntVar(1, 4, "CS101_time_slot")
CS102_time_slot = model.NewIntVar(1, 4, "CS102_time_slot")
AI201_time_slot = model.NewIntVar(1, 4, "AI201_time_slot")
DS202_time_slot = model.NewIntVar(1, 4, "DS202_time_slot")
SE301_time_slot = model.NewIntVar(1, 4, "SE301_time_slot")
ML401_time_slot = model.NewIntVar(1, 4, "ML401_time_slot")

CS101_room_no = model.NewIntVar(1, 3, "CS101_room_no")
CS102_room_no = model.NewIntVar(1, 3, "CS102_room_no")
AI201_room_no = model.NewIntVar(1, 3, "AI201_room_no")
DS202_room_no = model.NewIntVar(1, 3, "DS202_room_no")
SE301_room_no = model.NewIntVar(1, 3, "SE301_room_no")
ML401_room_no = model.NewIntVar(1, 3, "ML401_room_no")

# =========================
# CONSTRAINTS
# =========================

# time slot conflict constraints
model.Add(CS101_time_slot != CS102_time_slot)
model.Add(CS102_time_slot != AI201_time_slot)
model.Add(AI201_time_slot != ML401_time_slot)
model.Add(DS202_time_slot != SE301_time_slot)

# room capacity constraints (correct logic based on your encoding)
model.Add(CS102_room_no != 1)
model.Add(AI201_room_no != 1)
model.Add(DS202_room_no != 1)
model.Add(ML401_room_no == 3)

# additional constraints
model.AddAllowedAssignments([ML401_time_slot], [[3], [4]])
model.AddAllowedAssignments([DS202_time_slot], [[1], [2]])

# =========================
# MAPPING
# =========================
time = {
    "CS101": CS101_time_slot,
    "CS102": CS102_time_slot,
    "AI201": AI201_time_slot,
    "DS202": DS202_time_slot,
    "SE301": SE301_time_slot,
    "ML401": ML401_time_slot
}

room = {
    "CS101": CS101_room_no,
    "CS102": CS102_room_no,
    "AI201": AI201_room_no,
    "DS202": DS202_room_no,
    "SE301": SE301_room_no,
    "ML401": ML401_room_no
}

# =========================
# SAME ROOM CONSTRAINT
# =========================
courses = ["CS101", "CS102", "AI201", "DS202", "SE301", "ML401"]

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        c1 = courses[i]
        c2 = courses[j]

        same_room = model.NewBoolVar(f"same_room_{c1}_{c2}")

        model.Add(room[c1] == room[c2]).OnlyEnforceIf(same_room)
        model.Add(room[c1] != room[c2]).OnlyEnforceIf(same_room.Not())

        model.Add(time[c1] != time[c2]).OnlyEnforceIf(same_room)

# =========================
# SOLVER
# =========================
solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True


class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self,
                 CS101_time_slot, CS102_time_slot, AI201_time_slot,
                 DS202_time_slot, SE301_time_slot, ML401_time_slot,
                 CS101_room_no, CS102_room_no, AI201_room_no,
                 DS202_room_no, SE301_room_no, ML401_room_no):

        super().__init__()
        self.count = 0

        self.CS101_time_slot = CS101_time_slot
        self.CS102_time_slot = CS102_time_slot
        self.AI201_time_slot = AI201_time_slot
        self.DS202_time_slot = DS202_time_slot
        self.SE301_time_slot = SE301_time_slot
        self.ML401_time_slot = ML401_time_slot

        self.CS101_room_no = CS101_room_no
        self.CS102_room_no = CS102_room_no
        self.AI201_room_no = AI201_room_no
        self.DS202_room_no = DS202_room_no
        self.SE301_room_no = SE301_room_no
        self.ML401_room_no = ML401_room_no

    def OnSolutionCallback(self):
        self.count += 1
        print(f"\nSolution {self.count}:")

        print("CS101 -> Time:", self.Value(self.CS101_time_slot), "Room:", self.Value(self.CS101_room_no))
        print("CS102 -> Time:", self.Value(self.CS102_time_slot), "Room:", self.Value(self.CS102_room_no))
        print("AI201 -> Time:", self.Value(self.AI201_time_slot), "Room:", self.Value(self.AI201_room_no))
        print("DS202 -> Time:", self.Value(self.DS202_time_slot), "Room:", self.Value(self.DS202_room_no))
        print("SE301 -> Time:", self.Value(self.SE301_time_slot), "Room:", self.Value(self.SE301_room_no))
        print("ML401 -> Time:", self.Value(self.ML401_time_slot), "Room:", self.Value(self.ML401_room_no))


solution_printer = SolutionPrinter(
    CS101_time_slot, CS102_time_slot, AI201_time_slot,
    DS202_time_slot, SE301_time_slot, ML401_time_slot,
    CS101_room_no, CS102_room_no, AI201_room_no,
    DS202_room_no, SE301_room_no, ML401_room_no
)

solver.SearchForAllSolutions(model, solution_printer)

print("\nTotal solutions found:", solution_printer.count)