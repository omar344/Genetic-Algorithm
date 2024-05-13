def get_ga_config():
    """Get the configuration for the genetic algorithm"""
    population_size = 20 # Number of individuals in the population
    elitism_percentage = 0.2 # Percentage of the population to be selected for elitism
    tournament_size = 5 # Number of chromosomes to select for tournament
    max_generations = 100 # Number of generations to run the algorithm for
    max_stagnation = 20 # Number of generations to wait before terminating due to stagnation

    return population_size, elitism_percentage, tournament_size, max_generations, max_stagnation