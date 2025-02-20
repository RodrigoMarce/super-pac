import pulp

lp_problem = pulp.LpProblem("Final Project", pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound=100000, upBound=15000000, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=100000, upBound=15000000, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=100000, upBound=15000000, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=100000, upBound=15000000, cat='Continuous')
x5 = pulp.LpVariable('x5', lowBound=100000, upBound=15000000, cat='Continuous')
x6 = pulp.LpVariable('x6', lowBound=100000, upBound=15000000, cat='Continuous')
x7 = pulp.LpVariable('x7', lowBound=100000, upBound=15000000, cat='Continuous')
x8 = pulp.LpVariable('x8', lowBound=100000, upBound=15000000, cat='Continuous')
x9 = pulp.LpVariable('x9', lowBound=100000, upBound=15000000, cat='Continuous')
x10 = pulp.LpVariable('x10', lowBound=100000, upBound=15000000, cat='Continuous')
x11 = pulp.LpVariable('x11', lowBound=100000, upBound=15000000, cat='Continuous')
x12 = pulp.LpVariable('x12', lowBound=100000, upBound=15000000, cat='Continuous')
x13 = pulp.LpVariable('x13', lowBound=100000, upBound=15000000, cat='Continuous')
x14 = pulp.LpVariable('x14', lowBound=100000, upBound=15000000, cat='Continuous')
x15 = pulp.LpVariable('x15', lowBound=100000, upBound=15000000, cat='Continuous')
x16 = pulp.LpVariable('x16', lowBound=100000, upBound=15000000, cat='Continuous')
x17 = pulp.LpVariable('x17', lowBound=100000, upBound=15000000, cat='Continuous')
x18 = pulp.LpVariable('x18', lowBound=100000, upBound=15000000, cat='Continuous')
x19 = pulp.LpVariable('x19', lowBound=100000, upBound=15000000, cat='Continuous')
x20 = pulp.LpVariable('x20', lowBound=100000, upBound=15000000, cat='Continuous')
x21 = pulp.LpVariable('x21', lowBound=100000, upBound=15000000, cat='Continuous')
x22 = pulp.LpVariable('x22', lowBound=100000, upBound=15000000, cat='Continuous')
x23 = pulp.LpVariable('x23', lowBound=100000, upBound=15000000, cat='Continuous')
x24 = pulp.LpVariable('x24', lowBound=100000, upBound=15000000, cat='Continuous')
x25 = pulp.LpVariable('x25', lowBound=100000, upBound=15000000, cat='Continuous')
x26 = pulp.LpVariable('x26', lowBound=100000, upBound=15000000, cat='Continuous')
x27 = pulp.LpVariable('x27', lowBound=100000, upBound=15000000, cat='Continuous')
x28 = pulp.LpVariable('x28', lowBound=100000, upBound=15000000, cat='Continuous')
x29 = pulp.LpVariable('x29', lowBound=100000, upBound=15000000, cat='Continuous')
x30 = pulp.LpVariable('x30', lowBound=100000, upBound=15000000, cat='Continuous')
x31 = pulp.LpVariable('x31', lowBound=100000, upBound=15000000, cat='Continuous')
x32 = pulp.LpVariable('x32', lowBound=100000, upBound=15000000, cat='Continuous')
x33 = pulp.LpVariable('x33', lowBound=100000, upBound=15000000, cat='Continuous')
x34 = pulp.LpVariable('x34', lowBound=100000, upBound=15000000, cat='Continuous')
x35 = pulp.LpVariable('x35', lowBound=100000, upBound=15000000, cat='Continuous')
x36 = pulp.LpVariable('x36', lowBound=100000, upBound=15000000, cat='Continuous')
x37 = pulp.LpVariable('x37', lowBound=100000, upBound=15000000, cat='Continuous')
x38 = pulp.LpVariable('x38', lowBound=100000, upBound=15000000, cat='Continuous')
x39 = pulp.LpVariable('x39', lowBound=100000, upBound=15000000, cat='Continuous')
x40 = pulp.LpVariable('x40', lowBound=100000, upBound=15000000, cat='Continuous')
x41 = pulp.LpVariable('x41', lowBound=100000, upBound=15000000, cat='Continuous')
x42 = pulp.LpVariable('x42', lowBound=100000, upBound=15000000, cat='Continuous')
x43 = pulp.LpVariable('x43', lowBound=100000, upBound=15000000, cat='Continuous')
x44 = pulp.LpVariable('x44', lowBound=100000, upBound=15000000, cat='Continuous')
x45 = pulp.LpVariable('x45', lowBound=100000, upBound=15000000, cat='Continuous')
x46 = pulp.LpVariable('x46', lowBound=100000, upBound=15000000, cat='Continuous')
x47 = pulp.LpVariable('x47', lowBound=100000, upBound=15000000, cat='Continuous')
x48 = pulp.LpVariable('x48', lowBound=100000, upBound=15000000, cat='Continuous')
x49 = pulp.LpVariable('x49', lowBound=100000, upBound=15000000, cat='Continuous')
x50 = pulp.LpVariable('x50', lowBound=100000, upBound=15000000, cat='Continuous')
x51 = pulp.LpVariable('x51', lowBound=100000, upBound=15000000, cat='Continuous')

# Objective function
lp_problem += 9 * 0.76 * x1 + 3 * 0.91 * x2 + 11 * 0.986 * x3 + 6 * 0.85 * x4 + 54 * 0.751 * x5 + 10 * 0.9 * x6 + 7 * 0.84 * x7 + 3 * 0.83 * x8 + 3 * 0.15 * x9 + 30 * 0.975 * x10 + 16 * 0.988 * x11 + 4 * 0.657 * x12 + 4 * 0.819 * x13 + 19 * 0.84 * x14 + 11 * 0.892 * x15 + 6 * 0.987 * x16 + 6 * 0.871 * x17 + 8 * 0.843 * x18 + 8 * 0.794 * x19 + 4 * 0.87 * x20 + 10 * 0.686 * x21 + 11 * 0.642 * x22 + 15 * 0.921 * x23 + 10 * 0.908 * x24 + 6 * 0.841 * x25 + 10 * 0.92 * x26 + 4 * 0.956 * x27 + 5 * 0.962 * x28 + 6 * 0.947 * x29 + 4 * 0.889 * x30 + 14 * 0.796 * x31 + 5 * 0.883 * x32 + 28 * 0.706 * x33 + 16 * 0.982 * x34 + 3 * 0.827 * x35 + 17 * 0.992 * x36 + 7 * 0.77 * x37 + 8 * 0.787 * x38 + 19 * 0.953 * x39 + 4 * 0.694 * x40 + 9 * 0.929 * x41 + 3 * 0.846 * x42 + 11 * 0.863 * x43 + 40 * 0.989 * x44 + 6 * 0.902 * x45 + 3 * 0.613 * x46 + 13 * 0.882 * x47 + 12 * 0.77 * x48 + 4 * 0.714 * x49 + 10 * 0.916 * x50 + 3 * 0.685 * x51, "Objective Function"

# Budget constraint
lp_problem += x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 + x14 + x15 + x16 + x17 + x18 + x19 + x20 + x21 + x22 + x23 + x24 + x25 + x26 + x27 + x28 + x29 + x30 + x31 + x32 + x33 + x34 + x35 + x36 + x37 + x38 + x39 + x40 + x41 + x42 + x43 + x44 + x45 + x46 + x47 + x48 + x49 + x50 + x51 <= 100000000, "Total Budget Constraint"

# Swing state constraint
lp_problem += x23 + x50 + x39 + x34 + x11 + x3 + x29 == 70000000, "Swing State Constraint"


lp_problem.solve()

# Print the results
print("Status:", pulp.LpStatus[lp_problem.status])

sum = 0

for results in lp_problem.variables():
  print(results.name, "=", results.varValue)
  sum += results.varValue

print("Objective Value:", pulp.value(lp_problem.objective))

print("Total money spent:", sum)
