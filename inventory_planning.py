import numpy as np

# Parameters
max_stage = 3
max_production = 5
max_inventory = 4
infinity = 999

fixed_cost = 13
inventory_cost = 2
production_cost = 3
demand = 3

# Initializes the accumulative costs from current stage to max_stage
accumulative_cost_g = np.zeros(max_inventory + 1)

for stage in reversed(range(max_stage)):
    current_cost_g = np.zeros((max_inventory + 1, max_production + 1))
    for prod in range(max_production + 1):
        for inv_start in range(max_inventory + 1):
            # Updates inventory transition
            inv_end = inv_start + prod - demand
            # Computes costs for the current pair
            cost = infinity if inv_end < 0 else production_cost * prod + 0.5 * (inv_end + inv_start) * inventory_cost
            if prod > 0:
                cost += fixed_cost
            # Updates cost for all (inv, prod) pairs
            current_cost_g[inv_start, prod] = cost + accumulative_cost_g[
                inv_end] if inv_end <= max_inventory else infinity
    # Keeps record for the optimal production
    accumulative_cost_g = current_cost_g.min(axis=1)
    optimal_prod = current_cost_g.argmin(axis=1)
    # Prints outputs
    print(f"Date {stage + 1} \n"
          f"Inventory level: {list(range(max_inventory + 1))} \n"
          f"Optimal production: {optimal_prod}\n"
          f"Optimal cost: {accumulative_cost_g}\n")
