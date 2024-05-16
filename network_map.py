from library import *

def create_network_map(cities, cost_matrix, cities_coords):
    """Create a visual representation of the network"""

    # Calculate average latitude and longitude for the initial map center
    avg_lat = sum(coord['latitude'] for coord in cities_coords.values()) / len(cities_coords)
    avg_lon = sum(coord['longitude'] for coord in cities_coords.values()) / len(cities_coords)

    # Create a map centered around the average location
    map = folium.Map(location=[avg_lat, avg_lon], zoom_start=5)

    # Add markers for each city
    for city, coords in cities_coords.items():
        folium.Marker([coords['latitude'], coords['longitude']], popup=city).add_to(map)

    # Determine min and max costs for normalization
    min_cost = np.min(cost_matrix[cost_matrix != np.inf])
    max_cost = np.max(cost_matrix[cost_matrix != np.inf])

    # Function to normalize costs to a range for line widths
    def normalize_cost(cost, min_cost, max_cost, min_width=1, max_width=5):
        # Inverse normalization to make cheaper routes thicker
        return max_width - (cost - min_cost) * (max_width - min_width) / (max_cost - min_cost)

    line_color = '#69b8d6' # Color for the lines

    # Draw connections with varying line widths
    for i, city1 in enumerate(cities):
        for j, city2 in enumerate(cities):
            if i != j and cost_matrix.iloc[i, j] != np.inf:
                cost = cost_matrix.iloc[i, j]
                line_width = normalize_cost(cost, min_cost, max_cost)
                location1 = [cities_coords[city1]['latitude'], cities_coords[city1]['longitude']]
                location2 = [cities_coords[city2]['latitude'], cities_coords[city2]['longitude']]
                line = folium.PolyLine(locations=[location1, location2], weight=line_width, color=line_color)
                map.add_child(line)

    return map