import random
def tournament_selection(population, tournament_size):
    """Select two parents from the population using tournament selection"""
    selected_parents = []
    for _ in range(2): # Select two parents
        # Randomly select tournament_size chromosomes for the tournament
        tournament = random.sample(population, tournament_size)
        # Select the best chromosome from the tournament
        winner = min(tournament, key=lambda x: x['cost'])
        selected_parents.append(winner)
    return selected_parents