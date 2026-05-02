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