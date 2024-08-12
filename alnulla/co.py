from ortools.sat.python import cp_model

# Create a new CP-SAT model
model = cp_model.CpModel()

# Example variables
i = 1
j = 2

# Create a boolean variable j_before_i
j_before_i = model.NewBoolVar(f'j_before_i_{i}_{j}')
