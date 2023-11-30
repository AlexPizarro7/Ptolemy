from Dependencies.utilities import *

print("\nWelcome to Ptolemy. The free Astrology software.")

city = input("\nEnter the city: ")
country = input("Enter the country: ")

locations = get_coordinates(city, country)

if len(locations) == 1:
    selected_location = locations[0]
else:
    print("\nMultiple locations found:")
    for index, location in enumerate(locations, 1):
        print(f"{index}. {location.address}")
    choice = int(input("\nPlease choose the correct location by number: "))
    selected_location = locations[choice - 1]

# Extracting latitude and longitude from the selected location
location_latitude = selected_location.latitude
location_longitude = selected_location.longitude

choice = input(
    "\nWould you like to use the current date and time? (yes/no): \n")

if choice.lower() == "yes":
    jd, now = calculate_current_julian_day()
else:
    year = int(input("Enter the year (xxxx): "))
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day (1-31): "))
    hour = int(input("Enter the hour (1-12): "))
    minute = int(input("Enter the minute (0-59): "))
    am_pm = input("Enter either AM or PM: ").strip().upper()

    while am_pm not in ["AM", "PM"]:
        print("Invalid input. Please enter either 'AM' or 'PM'.")
        am_pm = input("Enter either AM or PM: ").strip().upper()

    jd, now = calculate_custom_julian_day(
        year, month, day, hour, minute, am_pm, location_latitude, location_longitude)

# Define the available house systems with enumeration for the user to choose from
house_systems = {
    '1': 'Placidus',
    '2': 'Whole Sign',
    '3': 'Regiomontanus',
}

# Display the house systems as a menu
print("\nThe following are the currently supported house systems: ")
for number, system in house_systems.items():
    print(f"{number}: {system}")

# Prompt the user to make a choice based on the menu
user_choice = input(
    "\nEnter the number of the house system you would like to use: ")

# Retrieve the house system corresponding to the user's choice
selected_house_system = house_systems[user_choice]

# Gets the house system code so we can use it as an argument in other functions
selected_house_system_code = get_house_system_code(selected_house_system)

# Calculate the ascendant
chart_ascendant = calculate_ascendant(
    jd, location_latitude, location_longitude, selected_house_system_code)

# Calculation of ecliptic longitude of planets
sun_longitude = calculate_ecliptic_longitude(
    "Sun", jd, location_latitude, location_longitude)
moon_longitude = calculate_ecliptic_longitude(
    "Moon", jd, location_latitude, location_longitude)
mercury_longitude = calculate_ecliptic_longitude(
    "Mercury", jd, location_latitude, location_longitude
)
venus_longitude = calculate_ecliptic_longitude(
    "Venus", jd, location_latitude, location_longitude
)
mars_longitude = calculate_ecliptic_longitude(
    "Mars", jd, location_latitude, location_longitude
)
jupiter_longitude = calculate_ecliptic_longitude(
    "Jupiter", jd, location_latitude, location_longitude
)
saturn_longitude = calculate_ecliptic_longitude(
    "Saturn", jd, location_latitude, location_longitude
)

# Calculation of what zodiac signs the planets are in
sun_sign = get_zodiac_sign(sun_longitude)
moon_sign = get_zodiac_sign(moon_longitude)
mercury_sign = get_zodiac_sign(mercury_longitude)
venus_sign = get_zodiac_sign(venus_longitude)
mars_sign = get_zodiac_sign(mars_longitude)
jupiter_sign = get_zodiac_sign(jupiter_longitude)
saturn_sign = get_zodiac_sign(saturn_longitude)

# Calculation of the sign degrees of the planets
sun_sign_degrees = get_sign_degrees(sun_longitude)
moon_sign_degrees = get_sign_degrees(moon_longitude)
mercury_sign_degrees = get_sign_degrees(mercury_longitude)
venus_sign_degrees = get_sign_degrees(venus_longitude)
mars_sign_degrees = get_sign_degrees(mars_longitude)
jupiter_sign_degrees = get_sign_degrees(jupiter_longitude)
saturn_sign_degrees = get_sign_degrees(saturn_longitude)


# Calculate house cusps
house_cusps = calculate_house_cusps(
    jd, location_latitude, location_longitude, selected_house_system_code)

print(
    f"\nEcliptic Longitude of the Sun: {float(sun_longitude):.2f} degrees."
    f"\nThe Sun is {float(sun_sign_degrees):.2f} degrees in {sun_sign}."

    f"\n\nEcliptic longitude of the Moon: {float(moon_longitude):.2f} degrees."
    f"\nThe Moon is {float(moon_sign_degrees):.2f} degrees in {moon_sign}."

    f"\n\nEcliptic longitude of Mercury: {float(mercury_longitude):.2f} degrees."
    f"\nMercury is {float(mercury_sign_degrees):.2f} degrees in {mercury_sign}."

    f"\n\nEcliptic longitude of Venus: {float(venus_longitude):.2f} degrees."
    f"\nVenus is {float(venus_sign_degrees):.2f} degrees in {venus_sign}."

    f"\n\nEcliptic longitude of Mars: {float(mars_longitude):.2f} degrees."
    f"\nMars is {float(mars_sign_degrees):.2f} degrees in {mars_sign}."

    f"\n\nEcliptic longitude of Jupiter: {float(jupiter_longitude):.2f} degrees."
    f"\nJupiter is {float(jupiter_sign_degrees):.2f} degrees in {jupiter_sign}."

    f"\n\nEcliptic longitude of Saturn: {float(saturn_longitude):.2f} degrees."
    f"\nSaturn is {float(saturn_sign_degrees):.2f} degrees in {saturn_sign}."
)


print(
    f"\nYour house system: {selected_house_system}."
    f"\nThe degree of the Ascendant is: {chart_ascendant}"
)

print(f"{house_cusps}")
