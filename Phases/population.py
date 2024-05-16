import random
def initialise_population(pop_size, cities, origin, destination):
    """Create a population of chromosomes"""
    population = []
    shortest_path_chromosome = {}
    longest_path_chromosome = {}

    # List all other cities besides the origin and destination
    connection_cities = [city for city in cities if city not in [origin, destination]]  # exclude origin and destination

    # Add a cromosome with the shortest path
    shortest_path_chromosome['route'] = [origin] + [destination]
    population.append(shortest_path_chromosome)

    # Add a chromosome with the longest path (going through all cities)
    longest_path_chromosome['route'] = [origin] + connection_cities + [destination]
    population.append(longest_path_chromosome)

    # Add chromosomes with random paths between origin and destination until we reach the total number of individuals in the population
    for _ in range(pop_size - 2):
        random_chromosome = {}
        # Randomly decide how many intermediate cities to include
        num_intermediate = random.randint(0, len(connection_cities) - 2)
        # Randomly select the intermediate cities
        intermediate_cities = random.sample(connection_cities, num_intermediate)
        # Build the chromosome
        random_chromosome['route'] = [origin] + intermediate_cities + [destination]
        # Add chromosome to population
        population.append(random_chromosome)

    return population