"""
A classroom consists of six students: Ali, Sara, Ahmed, Zoya, Bilal, and Hina—who need to be
seated in a row of six seats numbered from 1 to 6. The objective is to assign each student to exactly
one seat such that all seating constraints are satisfied. According to the requirements, Sara must sit
next to Zoya, meaning their seat numbers must be adjacent. Ali is not allowed to sit next to Ahmed,
so their assigned seats must not be consecutive. Bilal must be seated only in an even-numbered
seat (2, 4, or 6), while Hina cannot be assigned seat number 1. Additionally, each seat can be
occupied by only one student, and no student can occupy more than one seat. Students are required
to model this problem as a Constraint Satisfaction Problem (CSP) by defining appropriate variables
representing each student, specifying the domain of possible seat numbers for each variable, and
formally expressing all given constraints using mathematical or logical notation.
"""

from ortools.sat.python import cp_model

model = cp_model.CpModel()

Ali = model.new_int_var(1, 6, "Ali")
Sara = model.new_int_var(1, 6, "Sara")
Ahmed = model.new_int_var(1, 6, "Ahmed")
Zoya = model.new_int_var(1, 6, "Zoya")
Bilal = model.new_int_var(1, 6, "Bilal")
Hina = model.new_int_var(1, 6, "Hina")
sz_diff = model.new_int_var(0, 5, "sz_diff")
aa_diff = model.new_int_var(0, 5, "aa_diff")

model.add_abs_equality(sz_diff, Sara - Zoya)
model.add(sz_diff == 1)

model.add_abs_equality(aa_diff, Ali - Ahmed)
model.add(aa_diff != 1)
          
model.add_allowed_assignments([Bilal], [[2], [4], [6]])
model.add(Hina != 1)
model.AddAllDifferent([Ali, Sara, Ahmed, Zoya, Bilal, Hina])

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, Ali, Sara, Ahmed, Zoya, Bilal, Hina):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.Ali = Ali
        self.Sara = Sara
        self.Ahmed = Ahmed
        self.Zoya = Zoya
        self.Bilal = Bilal
        self.Hina = Hina
        self.count = 0

    def OnSolutionCallback(self):
        self.count += 1
        print(f"\nSolution {self.count}:")
        print("Ali:", self.Value(self.Ali))
        print("Sara:", self.Value(self.Sara))
        print("Ahmed:", self.Value(self.Ahmed))
        print("Zoya:", self.Value(self.Zoya))
        print("Bilal:", self.Value(self.Bilal))
        print("Hina:", self.Value(self.Hina))



solver = cp_model.CpSolver()

solver.parameters.enumerate_all_solutions = True

solution_printer = SolutionPrinter(Ali, Sara, Ahmed, Zoya, Bilal, Hina)

solver.SearchForAllSolutions(model, solution_printer)

print("\nTotal solutions found:", solution_printer.count)
