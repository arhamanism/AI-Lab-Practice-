"""
You are tasked with building a Bayesian Network to predict the likelihood of a disease
(e.g., Flu or Cold) based on the presence of various symptoms, including fever, cough,
fatigue, and chills. The network consists of the following nodes:
● Symptoms: Fever, Cough, Fatigue, Chills
● Disease: Flu, Cold

Network Structure:
The Disease node influences the symptoms: Fever, Cough, Fatigue, and Chills.
The Symptoms nodes are observed, and they are conditionally dependent on the Disease
node.

Prior Probabilities:
P(Disease):
1. P(Flu) = 0.3
2. P(Cold) = 0.7

P(Symptoms | Disease): (You are to define the following conditional probabilities based
on assumptions )

P(Fever | Disease):
1. P(Fever = Yes | Flu) = 0.9
2. P(Fever = Yes | Cold) = 0.5
3. P(Fever = No | Flu) = 0.1
4. P(Fever = No | Cold) = 0.5

P(Cough | Disease):
1. P(Cough = Yes | Flu) = 0.8
2. P(Cough = Yes | Cold) = 0.6
3. P(Cough = No | Flu) = 0.2
4. P(Cough = No | Cold) = 0.4

P(Fatigue | Disease):
1. P(Fatigue = Yes | Flu) = 0.7
2. P(Fatigue = Yes | Cold) = 0.3
3. P(Fatigue = No | Flu) = 0.3
4. P(Fatigue = No | Cold) = 0.7

P(Chills | Disease):
1. P(Chills = Yes | Flu) = 0.6
2. P(Chills = Yes | Cold) = 0.4
3. P(Chills = No | Flu) = 0.4
4. P(Chills = No | Cold) = 0.6

Construct the Bayesian Network:
Draw the structure of the Bayesian Network based on the dependencies given above.
Define the Conditional Probability Tables (CPTs)
Define reasonable CPTs for all nodes (Disease, Fever, Cough, Fatigue, and Chills) based
on the given probabilities. You may assume the probabilities if necessary.

Perform Inference Task 1:
Use the Bayesian Network to calculate the posterior probability of the Disease (Flu or
Cold), given the following symptoms:
● Fever = Yes
● Cough = Yes

Perform Inference Task 2:
Add a new symptom: Chills.
Update the Bayesian Network to compute the posterior probability of the Disease (Flu
or Cold), given the following symptoms:
● Fever = Yes
● Cough = Yes
● Chills = Yes

Perform Inference Task 3:
Given that the disease is Flu, calculate the probability that the person also has Fatigue.
● What is P(Fatigue = Yes | Disease = Flu)?
"""

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([("Disease", "Fever"),("Disease", "Cough"),("Disease", "Fatigue"),("Disease", "Chills")])

cpd_Disease = TabularCPD(
    variable="Disease",
    variable_card=2,
    values=[
        [0.3],
        [0.7]
    ],
    #state_names={"Disease": ["Flu", "Cold"]}
)

cpd_Fever = TabularCPD(
    variable="Fever", 
    variable_card=2,
    values=[
        [0.1, 0.5], #Fever No
        [0.9, 0.5]  #Fever Yes
    ],
    evidence=["Disease"],
    evidence_card=[2]
)

cpd_Cough = TabularCPD(
    variable="Cough", 
    variable_card=2,
    values=[
        [0.2, 0.4], #Cough No
        [0.8, 0.6]  #Cough Yes
    ],
    evidence=["Disease"],
    evidence_card=[2]
)

cpd_Fatigue = TabularCPD(
    variable="Fatigue", 
    variable_card=2,
    values=[
        [0.3, 0.7], #Fatigue No
        [0.7, 0.3]  #Fatigue Yes
    ],
    evidence=["Disease"],
    evidence_card=[2]
)

cpd_Chills = TabularCPD(
    variable="Chills", 
    variable_card=2,
    values=[
        [0.4, 0.6], #Chills No
        [0.6, 0.4]  #Chills Yes
    ],
    evidence=["Disease"],
    evidence_card=[2]
)

model.add_cpds(
    cpd_Disease,
    cpd_Fever,
    cpd_Cough,
    cpd_Fatigue,
    cpd_Chills
)

assert model.check_model()

inference = VariableElimination(model)

result1 = inference.query(
    variables=["Disease"],
    evidence={"Fever": 1, "Cough": 1}
)

result2 = inference.query(
    variables=["Disease"],
    evidence={"Fever": 1, "Cough": 1, "Chills": 1}
)

result3 = inference.query(
    variables=["Fatigue"],
    evidence={"Disease": 0}
)


print(result1)
print(result2)
print(result3)
