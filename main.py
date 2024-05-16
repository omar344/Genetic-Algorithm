from animation import animate_best_routes
from Phases.crossover import crossover
from data import get_data
from Phases.evaluate_population import evaluate_and_sort_population
from Phases.genatic_config import get_ga_config
from Phases.mutation import mutation
from network_map import create_network_map
from Phases.population import initialise_population
from Phases.tournament_selection import tournament_selection


def genetic_algorithm():
    """Run the genetic algorithm (GA)"""
    # Get data
    cities, origin, destination, handling_costs, cost_matrix, cities_coords = get_data()

    # Create visual representation of network (Optional)
    map = create_network_map(cities, cost_matrix, cities_coords)
    # Save the map to an HTML file
    map.save('./assets/network_map.html')

    # Get GA configurations
    population_size, elitism_percentage, tournament_size, max_generations, max_stagnation = get_ga_config()

    # Initialise population
    population = initialise_population(population_size, cities, origin, destination)
    # Evaluate and sort the initial population
    population = evaluate_and_sort_population(population, cost_matrix, handling_costs)

    # Stagnation variables
    best_cost = float('inf')
    stagnation_counter = 0

    # Store best route for visualisation purposes
    best_routes_per_generation = []

    # Main GA loop
    for generation in range(max_generations):
        new_population = []

        # Apply elitism - select the best chromosomes from the population
        elite_chromosomes = population[:int(elitism_percentage * population_size)]
        new_population.extend(elite_chromosomes)

        while len(new_population) < population_size:
            # Apply tournament selection
            parent1, parent2 = tournament_selection(population, tournament_size)

            # Create new chromosomes applying crossover
            offspring1, offspring2 = crossover(parent1, parent2, origin, destination)

            # Create new chromosomes applying mutation to the new offsprings
            offspring3, offspring4 = mutation(offspring1, cities, origin, destination)

            # Add offsprings to new population
            new_population.extend([offspring1, offspring2, offspring3, offspring4])

        population = new_population
        population = evaluate_and_sort_population(population, cost_matrix, handling_costs)

        # Get best route
        best_chromosome = population[0]
        best_routes_per_generation.append((best_chromosome['route'], best_chromosome['cost']))

        # Check for stagnation
        current_best_cost = best_chromosome['cost']  # Population is sorted in ascending order of cost
        if current_best_cost < best_cost:
            best_cost = current_best_cost
            print(f'Generation {generation} best cost {best_cost}')
            stagnation_counter = 0  # Reset stagnation counter
        else:
            stagnation_counter += 1

        if stagnation_counter >= max_stagnation:
            print(f"Terminating due to stagnation at generation {generation}.")
            break

    if generation == max_generations - 1:
        print(f"Info: Terminating due to reaching maximum of {generation} generations.")

    print(f"Info: Best cost found: {best_cost}")
    print(f"Info: Best route found: {best_chromosome['route']}")

    # Create animation to show best route evolving with generations
    gif_path = animate_best_routes(best_routes_per_generation, cities, cost_matrix, cities_coords)

    print(f"Info: Animation of best route evolution is available in: {gif_path}")

    return


if __name__ == "__main__":
    genetic_algorithm()