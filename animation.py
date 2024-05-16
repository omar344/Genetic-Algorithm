from Libraries import * 
def animate_best_routes(best_routes_per_generation, cities, cost_matrix, cities_coords):
    """Create an animation to show the best route evolving with generations"""
    # Generate the frames
    images_paths = []
    unique_best_routes = [] # to avoid repeated routes in best_routes_per_generation
    _ = [unique_best_routes.append(x) for x in best_routes_per_generation if x not in unique_best_routes]

    # Use this for a GIF with all best route solutions
    for frame, (route, cost) in enumerate(best_routes_per_generation):

    # # Use this, instead, for a GIF with only unique solutions
    # for frame, (route, cost) in enumerate(unique_best_routes):

        map = create_network_map(cities, cost_matrix, cities_coords)

        route_colour = '#004E6B' # Color for the route
        # Add the evolving route for this generation to the map
        route_coords = [[cities_coords[city]['latitude'], cities_coords[city]['longitude']] for city in route]
        folium.PolyLine(route_coords, color=route_colour, weight=5, opacity=1).add_to(map)

        # Calculate average latitude and longitude for legend
        avg_lat = sum(coord['latitude'] for coord in cities_coords.values()) / len(cities_coords)
        avg_lon = sum(coord['longitude'] for coord in cities_coords.values()) / len(cities_coords)
        # Add a legend with the cost
        legend_html = f'''
            <div style="position: fixed; 
                        bottom: -250px; left: 220px; width: 150px; height: 90px; 
                        border:2px solid grey; z-index:9999; font-size:14px;
                        background-color:white; padding:10px;">
                <b>Cost: {cost}</b><br>
                Best solution in Generation {frame}
            </div>
        '''
        iframe = IFrame(legend_html, width=170, height=110)
        folium.Marker(location=[avg_lat, avg_lon], icon=folium.DivIcon(html=legend_html)).add_to(map)

        # Save the map as an HTML file for this frame
        html_path = f'./assets/frame_{frame}.html'  # Remove the leading "./assets" from the file path
        map.save(html_path)
        # Append image path to list
        image_path = f'./assets/frame_{frame}.png'  # Remove the leading "./" from the file path
        images_paths = images_paths + [image_path]

        convert_html_to_image(html_path, image_path)
        # Optionally delete html file
        os.remove(html_path)

    gif_path = f'./assets/{best_routes_per_generation[0][0][0]}_{best_routes_per_generation[0][0][-1]}.gif'  # Remove the leading "./" from the file path
    create_gif(images_paths, gif_path)

    # Optionally delete the image files after creating the GIF
    for image_path in images_paths:
        os.remove(image_path)

    return gif_path


def convert_html_to_image(html_path, image_path):
    """Convert an HTML file to an image and save it"""
    # Set up headless Chromium options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location += "./chrome-win64/chrome.exe"

    # Specify the path to chromedriver using Service
    service = Service(executable_path="chrome-win64/chromedriver.exe")

    # Initialize the driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Load the HTML file
    absolute_html_path = os.path.abspath(html_path)
    driver.get("file://" + absolute_html_path)

    # # If image is blank, wait for the content to load
    # time.sleep(1)  # Adjust the time as needed

    # Set the size of the window to capture the entire page
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(total_width, total_height)

    # Take a screenshot and save it
    screenshot = driver.get_screenshot_as_png()
    driver.quit()

    # Convert screenshot to an image and save
    image = Image.open(io.BytesIO(screenshot))
    image.save(image_path)

def create_gif(images_paths, gif_path):
    """Create a GIF from a list of image paths"""
    images = [Image.open(image) for image in images_paths]

    # Set the duration for each frame (in milliseconds)
    default_duration = 300  # Duration for all frames except the last one
    durations = [default_duration] * (len(images) - 1)  # Apply default duration to all frames except the last
    durations.append(2000)  # Higher duration for the last frame so that end of loop in GIF is obvious

    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=durations, loop=0)