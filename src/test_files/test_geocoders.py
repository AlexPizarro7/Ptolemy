from geopy.geocoders import Nominatim


def get_coordinates(city, country):
    # Initializes Nominatim geocoder, user_agent is required as it identifies you to the service
    geolocator = Nominatim(user_agent="AstrologyApp")
    # Sends request to the service to translate the city and country names to coordinates
    # exactly_one=False ensures it returns all matches
    locations = geolocator.geocode(f"{city}, {country}", exactly_one=False)
    return locations


city = input("\nEnter the city: ")
country = input("Enter the country: ")

# Get the list of matching locations
locations = get_coordinates(city, country)

# If there's only one result, no need to ask the user
if len(locations) == 1:
    selected_location = locations[0]
else:
    # If multiple matches, print out the results and ask the user to choose
    print("\nMultiple locations found:")
    # Loops through the list, keeps track of the current item. The 1 indicates enumeration should start from 1
    for index, location in enumerate(locations, 1):
        print(f"{index}. {location.address}")
    # choice variable is an int input by the user
    choice = int(input("\nPlease choose the correct location by number: "))
    # Enumerates from 1, but indexes start at 0
    selected_location = locations[choice - 1]

print(
    f"\nCoordinates for {selected_location.address}: {selected_location.latitude}, {selected_location.longitude}")
