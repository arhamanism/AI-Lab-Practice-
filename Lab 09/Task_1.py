"""
You are given the following Bayesian Network structure to model student exam
performance:
Nodes:
● Intelligence (I) — {High, Low}
● StudyHours (S) — {Sufficient, Insufficient}
● Difficulty (D) — {Hard, Easy}
● Grade (G) — {A, B, C}
● Pass (P) — {Yes, No}

Dependencies:
Intelligence, StudyHours, and Difficulty directly affect Grade.
Grade directly affects Pass.
Prior Probabilities:
● P(Intelligence = High) = 0.7, P(Intelligence = Low) = 0.3
● P(StudyHours = Sufficient) = 0.6, P(StudyHours = Insufficient) = 0.4
● P(Difficulty = Hard) = 0.4, P(Difficulty = Easy) = 0.6

Conditional Probabilities (examples):
P(Grade | Intelligence, StudyHours, Difficulty):
(Assume your own valid values, e.g., students with High intelligence, Sufficient study
hours, and Easy difficulty are most likely to get A)
● P(Pass | Grade):
● P(Pass = Yes | Grade = A) = 0.95
● P(Pass = Yes | Grade = B) = 0.80
● P(Pass = Yes | Grade = C) = 0.50

Tasks to do
● Construct the Bayesian Network structure diagram showing all dependencies.
● Define the complete Conditional Probability Tables (CPTs) for all nodes.
● Implement the Bayesian Network using Python (pgmpy or equivalent).
● Perform inference using Variable Elimination to answer:
● What is the probability that the student passes the exam, given:
StudyHours = Sufficient,
Difficulty = Hard
● What is the probability that the student has High Intelligence, given:
Pass = Yes
"""

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Intelligence', 'Grade'), ('StudyHours', 'Grade'), ('Difficulty', 'Grade'), ('Grade', 'Pass')])

#P(Intelligence)
cpd_intelligence = TabularCPD(variable="Intelligence",variable_card=2, values=[[0.3], [0.7]])

#P(StudyHours)
cpd_studyhours = TabularCPD(variable="StudyHours",variable_card=2, values=[[0.4], [0.6]])

#P(Difficulty)
cpd_difficulty = TabularCPD(variable="Difficulty",variable_card=2, values=[[0.4], [0.6]])

#P(Grade|Intelligence, StudyHours, Difficulty)
cpd_grade = TabularCPD(
    variable="Grade", 
    variable_card=3, 
    values=[#A
             [0.95, 0.90, 0.85, 0.80, 0.70, 0.60, 0.50, 0.40],
            #B
             [0.04, 0.07, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35],
            #C
            [0.01, 0.03, 0.05, 0.05, 0.10, 0.15, 0.20, 0.25]
            ],
    evidence=["Intelligence", "StudyHours", "Difficulty"],
    evidence_card=[2,2,2]
)

cpd_pass = TabularCPD(
    variable="Pass",
    variable_card=2,
    values=[
        [0.05, 0.20, 0.50],
        [0.95, 0.80, 0.50]
    ],
    evidence=["Grade"],
    evidence_card=[3]
)

model.add_cpds(
    cpd_difficulty,
    cpd_intelligence,
    cpd_studyhours,
    cpd_grade,
    cpd_pass
)

assert model.check_model()

inference = VariableElimination(model)

result1 = inference.query(
    variables=["Pass"],
    evidence={"StudyHours" : 1, "Difficulty": 0}
)

result2 = inference.query(
    variables=["Intelligence"],
    evidence={"Pass" : 1}
)

print(f"P(Pass = Yes|StudyHours = Sufficient, Difficulty = Hard): {result1}")
print(f"P(Intelligence = High|Pass = Yes): {result2}")

