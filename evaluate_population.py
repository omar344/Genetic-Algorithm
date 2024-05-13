def evaluate_and_sort_population(population, cost_matrix, handling_costs):
    """Evaluate the population and sort it in ascending order of cost"""
    for chromosome in population:
        if 'cost' not in chromosome.keys():
            total_cost = 0
            for i in range(len(chromosome['route'])-1):
                city1 = chromosome['route'][i]
                city2 = chromosome['route'][i + 1]
                total_cost += cost_matrix.loc[city1, city2] + handling_costs[city1]
            chromosome['cost'] = total_cost
    return sorted(population, key=lambda x: x['cost'])