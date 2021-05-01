import pulp
import pulp as pl


solver = pl.getSolver('PULP_CBC_CMD')

lp_problem = pl.LpProblem(name="Product Mix", sense=pl.LpMaximize)

# Decision variables

x_a = pl.LpVariable(name="No. of Product A", lowBound=0, cat=pulp.LpInteger)
x_b = pl.LpVariable(name="No. of Product B", lowBound=0, cat=pulp.LpInteger)
x_c = pl.LpVariable(name="No. of Product C", lowBound=0, cat=pulp.LpInteger)
x_d = pl.LpVariable(name="No. of Product D", lowBound=0, cat=pulp.LpInteger)
x_e = pl.LpVariable(name="No. of Product E", lowBound=0, cat=pulp.LpInteger)

# Objectives
lp_problem += x_a*550 + x_b*600 + x_c*350 + x_d*400 + x_e*200, "Maximise revenue of the products."

# Constraints
lp_problem += 10*x_a + 20*x_b + 25*x_d + 15*x_e <= 288, "Grinding hours cannot exceed maximum available hours"
lp_problem += 10*x_a + 8*x_b + 16*x_c <= 192, "Drilling hours cannot exceed maximum available hours."
lp_problem += 20*x_a + 20*x_b + 20*x_c + 20*x_d + 20*x_e <= 384, "Assembly hours cannot exceed maximum available hours."

lp_problem.writeLP("product_mix_model.lp")
lp_problem.solve()
print("Status: ", pl.LpStatus[lp_problem.status])

for v in lp_problem.variables():
    print(v.name, "=", v.varValue)