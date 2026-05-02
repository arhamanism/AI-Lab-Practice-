"""
A logistics company is responsible for assigning delivery tasks to a fleet of vehicles. The company
has three vehicles: V1, V2, and V3—and five delivery locations labeled L1 through L5. Each
delivery location must be assigned to exactly one vehicle. However, the assignment must satisfy
several operational constraints. Each vehicle has a limited delivery capacity: V1 and V2 can handle
at most two deliveries each, while V3 can handle up to three deliveries. Additionally, certain
assignments are restricted: locations L1 and L2 cannot be assigned to the same vehicle, and
location L3 must be assigned specifically to vehicle V3.
To ensure fairness in workload distribution, the difference in the number of deliveries assigned to
V1 and V2 must not exceed one. Furthermore, there is a dependency constraint: if location L4 is
assigned to vehicle V1, then location L5 must also be assigned to V1. This problem can be modeled
as a Constraint Satisfaction Problem (CSP) where each location (l) is represented by a variable
(vehicle[l] in {V1, V2, V3}). Students are required to implement a function
solve_vehicle_assignment() using the OR-Tools CP-SAT solver. The solution should incorporate
counting constraints for vehicle capacities, logical implication constraints for dependencies, and
balancing constraints for workload distribution, and produce a valid assignment of locations to
vehicles as output.
"""