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