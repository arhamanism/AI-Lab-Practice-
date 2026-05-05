# =========================
# 1. IMPORT LIBRARIES
# =========================
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# =========================
# 2. DEFINE NETWORK STRUCTURE
# =========================
model = DiscreteBayesianNetwork([
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'JohnCalls'),
    ('Alarm', 'MaryCalls')
])

# =========================
# 3. DEFINE CPDs
# =========================

# P(Burglary)
cpd_burglary = TabularCPD(
    variable='Burglary',
    variable_card=2,
    values=[[0.999], [0.001]]
)

# P(Earthquake)
cpd_earthquake = TabularCPD(
    variable='Earthquake',
    variable_card=2,
    values=[[0.998], [0.002]]
)

# P(Alarm | Burglary, Earthquake)
cpd_alarm = TabularCPD(
    variable='Alarm',
    variable_card=2,
    values=[
        [0.999, 0.71, 0.06, 0.05],  # Alarm = False
        [0.001, 0.29, 0.94, 0.95]   # Alarm = True
    ],
    evidence=['Burglary', 'Earthquake'],
    evidence_card=[2, 2]
)

# P(JohnCalls | Alarm)
cpd_john = TabularCPD(
    variable='JohnCalls',
    variable_card=2,
    values=[
        [0.3, 0.9],  # JohnCalls = False
        [0.7, 0.1]   # JohnCalls = True
    ],
    evidence=['Alarm'],
    evidence_card=[2]
)

# P(MaryCalls | Alarm)
cpd_mary = TabularCPD(
    variable='MaryCalls',
    variable_card=2,
    values=[
        [0.2, 0.99],  # MaryCalls = False
        [0.8, 0.01]   # MaryCalls = True
    ],
    evidence=['Alarm'],
    evidence_card=[2]
)

# =========================
# 4. ADD CPDs TO MODEL
# =========================
model.add_cpds(
    cpd_burglary,
    cpd_earthquake,
    cpd_alarm,
    cpd_john,
    cpd_mary
)

# =========================
# 5. VERIFY MODEL
# =========================
assert model.check_model(), "Model is incorrect!"

# =========================
# 6. PERFORM INFERENCE
# =========================
inference = VariableElimination(model)

# =========================
# 7. QUERY
# =========================
result = inference.query(
    variables=['Burglary'],
    evidence={'JohnCalls': 1, 'MaryCalls': 1}
)

# =========================
# 8. OUTPUT RESULT
# =========================
print("Probability of Burglary given John and Mary called:\n")
print(result)
