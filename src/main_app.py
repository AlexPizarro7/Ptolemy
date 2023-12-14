from dependencies.astro_calculations import *
from dependencies.astro_utils import *

print("\nWelcome to Ptolemy. The free Astrology software.")

# Ask for a city and country anywhere in the world
city = input("\nEnter the city: ")
country = input("Enter the country: ")

# In the case there is multiple cities of the same name in the same country
locations = get_coordinates(city, country)
if len(locations) == 1:
    selected_location = locations[0]
else:
    print("\nMultiple locations found:")
    for index, location in enumerate(locations, 1):
        print(f"{index}. {location.address}")
    choice = int(input("\nPlease choose the correct location by number: "))
    selected_location = locations[choice - 1]

# Extracting latitude and longitude coordinates from the selected location
location_latitude = selected_location.latitude
location_longitude = selected_location.longitude

# Making a jd (julian day) based on either current date or time, or a custom one
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

# Calculate the ecliptic longitude of the planets
sun_longitude = calculate_ecliptic_longitude(
    'Sun', jd, location_latitude, location_longitude)
moon_longitude = calculate_ecliptic_longitude(
    'Moon', jd, location_latitude, location_longitude)
mercury_longitude = calculate_ecliptic_longitude(
    'Mercury', jd, location_latitude, location_longitude)
venus_longitude = calculate_ecliptic_longitude(
    'Venus', jd, location_latitude, location_longitude)
mars_longitude = calculate_ecliptic_longitude(
    'Mars', jd, location_latitude, location_longitude)
jupiter_longitude = calculate_ecliptic_longitude(
    'Jupiter', jd, location_latitude, location_longitude)
saturn_longitude = calculate_ecliptic_longitude(
    'Saturn', jd, location_latitude, location_longitude)

# Calculate the ecliptic longitude of the ascendant, and its sign and sign degrees
ascendant_longitude = calculate_ascendant(
    jd, location_latitude, location_longitude, selected_house_system_code)
ascendant_sign_degrees = get_sign_degrees(ascendant_longitude)
ascendant_sign = get_zodiac_sign(ascendant_longitude)

# Calculate house cusps
house_cusps = calculate_house_cusps(
    jd, location_latitude, location_longitude, selected_house_system_code)

# Determines if day or night chart
chart_time_type = is_day_chart(sun_longitude, ascendant_longitude)

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

# Calculation of the the bounds that the planets are in
sun_bound = get_ptolemaic_bound_ruler(sun_sign, sun_sign_degrees)
moon_bound = get_ptolemaic_bound_ruler(moon_sign, moon_sign_degrees)
mercury_bound = get_ptolemaic_bound_ruler(mercury_sign, mercury_sign_degrees)
venus_bound = get_ptolemaic_bound_ruler(venus_sign, venus_sign_degrees)
mars_bound = get_ptolemaic_bound_ruler(mars_sign, mars_sign_degrees)
jupiter_bound = get_ptolemaic_bound_ruler(jupiter_sign, jupiter_sign_degrees)
saturn_bound = get_ptolemaic_bound_ruler(saturn_sign, saturn_sign_degrees)

# calculation of the decans that the planets are in
sun_decan = get_traditional_decan(sun_sign, sun_sign_degrees)
moon_decan = get_traditional_decan(moon_sign, moon_sign_degrees)
mercury_decan = get_traditional_decan(mercury_sign, mercury_sign_degrees)
venus_decan = get_traditional_decan(venus_sign, venus_sign_degrees)
mars_decan = get_traditional_decan(mars_sign, mars_sign_degrees)
jupiter_decan = get_traditional_decan(jupiter_sign, jupiter_sign_degrees)
saturn_decan = get_traditional_decan(saturn_sign, saturn_sign_degrees)

# Sun dignity Analysis
sun_in_domicile = is_planet_in_its_traditional_domicile('Sun', sun_sign)
sun_in_exaltation = is_planet_in_its_traditional_exaltation('Sun', sun_sign)
sun_is_super_exalted = is_planet_super_exalted(
    'Sun', sun_sign, sun_sign_degrees)
sun_in_triplicity = is_planet_in_its_triplicity(
    'Sun', sun_sign, chart_time_type)
sun_in_detriment = is_planet_in_its_traditional_detriment('Sun', sun_sign)
sun_in_fall = is_planet_in_its_traditional_fall('Sun', sun_sign)

# Moon dignity analysis
moon_in_domicile = is_planet_in_its_traditional_domicile('Moon', moon_sign)
moon_in_exaltation = is_planet_in_its_traditional_exaltation('Moon', moon_sign)
moon_is_super_exalted = is_planet_super_exalted(
    'Moon', moon_sign, moon_sign_degrees)
moon_in_triplicity = is_planet_in_its_triplicity(
    'Moon', moon_sign, chart_time_type)
moon_in_detriment = is_planet_in_its_traditional_detriment('Moon', moon_sign)
moon_in_fall = is_planet_in_its_traditional_fall('Moon', moon_sign)

# Mercury dignity analysis
mercury_in_domicile = is_planet_in_its_traditional_domicile(
    'Mercury', mercury_sign)
mercury_in_exaltation = is_planet_in_its_traditional_exaltation(
    'Mercury', mercury_sign)
mercury_is_super_exalted = is_planet_super_exalted(
    'Mercury', mercury_sign, mercury_sign_degrees)
mercury_in_triplicity = is_planet_in_its_triplicity(
    'Mercury', mercury_sign, chart_time_type)
mercury_in_detriment = is_planet_in_its_traditional_detriment(
    'Mercury', mercury_sign)
mercury_in_fall = is_planet_in_its_traditional_fall('Mercury', mercury_sign)

# Venus dignity analysis
venus_in_domicile = is_planet_in_its_traditional_domicile('Venus', venus_sign)
venus_in_exaltation = is_planet_in_its_traditional_exaltation(
    'Venus', venus_sign)
venus_is_super_exalted = is_planet_super_exalted(
    'Venus', venus_sign, venus_sign_degrees)
venus_in_triplicity = is_planet_in_its_triplicity(
    'Venus', venus_sign, chart_time_type)
venus_in_detriment = is_planet_in_its_traditional_detriment(
    'Venus', venus_sign)
venus_in_fall = is_planet_in_its_traditional_fall('Venus', venus_sign)

# Mars dignity analysis
mars_in_domicile = is_planet_in_its_traditional_domicile('Mars', mars_sign)
mars_in_exaltation = is_planet_in_its_traditional_exaltation('Mars', mars_sign)
mars_is_super_exalted = is_planet_super_exalted(
    'Mars', mars_sign, mars_sign_degrees)
mars_in_triplicity = is_planet_in_its_triplicity(
    'Mars', mars_sign, chart_time_type)
mars_in_detriment = is_planet_in_its_traditional_detriment('Mars', mars_sign)
mars_in_fall = is_planet_in_its_traditional_fall('Mars', mars_sign)

# Jupiter dignity analysis
jupiter_in_domicile = is_planet_in_its_traditional_domicile(
    'Jupiter', jupiter_sign)
jupiter_in_exaltation = is_planet_in_its_traditional_exaltation(
    'Jupiter', jupiter_sign)
jupiter_is_super_exalted = is_planet_super_exalted(
    'Jupiter', jupiter_sign, jupiter_sign_degrees)
jupiter_in_triplicity = is_planet_in_its_triplicity(
    'Jupiter', jupiter_sign, chart_time_type)
jupiter_in_detriment = is_planet_in_its_traditional_detriment(
    'Jupiter', jupiter_sign)
jupiter_in_fall = is_planet_in_its_traditional_fall('Jupiter', jupiter_sign)

# Saturn dignity analysis
saturn_in_domicile = is_planet_in_its_traditional_domicile(
    'Saturn', saturn_sign)
saturn_in_exaltation = is_planet_in_its_traditional_exaltation(
    'Saturn', saturn_sign)
saturn_is_super_exalted = is_planet_super_exalted(
    'Saturn', saturn_sign, saturn_sign_degrees)
saturn_in_triplicity = is_planet_in_its_triplicity(
    'Saturn', saturn_sign, chart_time_type)
saturn_in_detriment = is_planet_in_its_traditional_detriment(
    'Saturn', saturn_sign)
saturn_in_fall = is_planet_in_its_traditional_fall('Saturn', saturn_sign)


# Print the Report details

print(f"\nAstrologial Report")

print(f"\nThe Sun ☉")
print(f"The Sun's ecliptic longitude: {float(sun_longitude):.2f} degrees.")
print(f"The Sun is {float(sun_sign_degrees):.2f} degrees in {sun_sign}.")
print(f"The Sun is in the Bound ruled by {sun_bound}.")
print(f"The Sun is in the Decan ruled by {sun_decan}.")

print(f"\nNotes on the Sun's dignity: ")

if sun_in_domicile:
    print(f"The Sun is in its own Domicile")

if sun_in_exaltation:
    print(f"The Sun is in its sign of Exaltation")

if sun_is_super_exalted:
    print(f"The Sun is in its super Exaltation degree")

if sun_in_triplicity:
    print(f"The Sun is in its own Triplicity sign")

if sun_bound == 'Sun':
    print(f"The Sun is in its own Bound")

if sun_decan == 'Sun':
    print(f"The Sun is in its own Decan")

if sun_in_detriment:
    print(f"The Sun is in its Detriment")

if sun_in_fall:
    print(f"The Sun is in its Fall")

if not any([sun_in_domicile, sun_in_exaltation, sun_is_super_exalted,
            sun_in_triplicity, sun_bound == 'Sun', sun_decan == 'Sun',
            sun_in_detriment, sun_in_fall]):
    print(f"The Sun is Peregrine")

print(f"\nThe Moon ☽")
print(f"The Moon's ecliptic longitude: {float(moon_longitude):.2f} degrees.")
print(f"The Moon is {float(moon_sign_degrees):.2f} degrees in {moon_sign}.")
print(f"The Moon is in the Bound ruled by {moon_bound}")
print(f"The Moon is in the Decan ruled by {moon_decan}")

print(f"\nNotes on the Moon's dignity: ")

if moon_in_domicile:
    print(f"The Moon is in its own Domicile.")

if moon_in_exaltation:
    print(f"The Moon is in its own sign of Exaltation.")

if moon_is_super_exalted:
    print(f"The Moon is in its super Exaltation degrees.")

if moon_in_triplicity:
    print(f"The Moon is in its own Triplicity sign.")

if moon_bound == 'Moon':
    print(f"The Moon is in its own Bound")

if moon_decan == 'Moon':
    print(f"The Moon is in its own Decan")

if moon_in_detriment:
    print(f"The Moon is in its Detriment")

if moon_in_fall:
    print(f"The moon is in its own Fall.")

if not any([moon_in_domicile, moon_in_exaltation, moon_is_super_exalted,
            moon_in_triplicity, moon_bound == 'Moon', moon_decan == 'Moon',
            moon_in_detriment, moon_in_fall]):
    print(f"The Moon is Peregrine")

print(f"\nMercury ☿")
print(f"Mercury's ecliptic longitude: {float(mercury_longitude):.2f} degrees.")
print(f"Mercury is {float(mercury_sign_degrees)
      :.2f} degrees in {mercury_sign}.")
print(f"Mercury is in in the bound of {mercury_bound}")
print(f"Mercury is in the decan of {mercury_decan}")

print(f"\nNotes on Mercury's dignity: ")

if mercury_in_domicile:
    print(f"Mercury is in its own Domicile.")

if mercury_in_exaltation:
    print(f"Mercury is in its own sign of Exaltation.")

if mercury_is_super_exalted:
    print(f"Mercury is in its super Exaltation degrees.")

if mercury_in_triplicity:
    print(f"Mercury is in its own Triplicity sign.")

if mercury_bound == 'Mercury':
    print(f"Mercury is in its own Bound")

if mercury_decan == 'Mercury':
    print(f"Mercury is in its own Decan")

if mercury_in_detriment:
    print(f"Mercury is in its Detriment")

if mercury_in_fall:
    print(f"Mercury is in its own Fall.")

if not any([mercury_in_domicile, mercury_in_exaltation, mercury_is_super_exalted,
            mercury_in_triplicity, mercury_bound == 'Mercury', mercury_decan == 'Mercury',
            mercury_in_detriment, mercury_in_fall]):
    print(f"Mercury is Peregrine")

print(f"\nVenus ♀")
print(f"Venus' ecliptic longitude: {float(venus_longitude):.2f} degrees.")
print(f"Venus is {float(venus_sign_degrees):.2f} degrees in {venus_sign}.")
print(f"Venus is in the bound of {venus_bound}")
print(f"Venus is in the decan of {venus_decan}")

print(f"\nNotes on Venus' dignity: ")

if venus_in_domicile:
    print(f"Venus is in its own Domicile.")

if venus_in_exaltation:
    print(f"Venus is in its own sign of Exaltation.")

if venus_is_super_exalted:
    print(f"Venus is in its super Exaltation degrees.")

if venus_in_triplicity:
    print(f"Venus is in its own Triplicity sign.")

if venus_bound == 'Venus':
    print(f"Venus is in its own Bound")

if venus_decan == 'Venus':
    print(f"Venus is in its own Decan")

if venus_in_detriment:
    print(f"Venus is in its Detriment")

if venus_in_fall:
    print(f"Venus is in its own Fall.")

if not any([venus_in_domicile, venus_in_exaltation, venus_is_super_exalted,
            venus_in_triplicity, venus_bound == 'Venus', venus_decan == 'Venus',
            venus_in_detriment, venus_in_fall]):
    print(f"Venus is Peregrine")

print(f"\nMars ♂")
print(f"Mars' ecliptic longitude: {float(mars_longitude):.2f} degrees.")
print(f"Mars is {float(mars_sign_degrees):.2f} degrees in {mars_sign}.")
print(f"Mars is in the bound of {mars_bound}")
print(f"Mars is in the decan of {mars_decan}")

print(f"\nNotes on Mars' dignity: ")

if mars_in_domicile:
    print(f"Mars is in its own Domicile.")

if mars_in_exaltation:
    print(f"Mars is in its own sign of Exaltation.")

if mars_is_super_exalted:
    print(f"Mars is in its super Exaltation degrees.")

if mars_in_triplicity:
    print(f"Mars is in its own Triplicity sign.")

if mars_bound == 'Mars':
    print(f"Mars is in its own Bound")

if mars_decan == 'Mars':
    print(f"Mars is in its own Decan")

if mars_in_detriment:
    print(f"Mars is in its Detriment")

if mars_in_fall:
    print(f"Mars is in its own Fall.")

if not any([mars_in_domicile, mars_in_exaltation, mars_is_super_exalted,
            mars_in_triplicity, mars_bound == 'Mars', mars_decan == 'Mars',
            mars_in_detriment, mars_in_fall]):
    print(f"Mars is Peregrine")

print(f"\nJupiter ♃")
print(f"Jupiter's ecliptic longitude: {
      float(jupiter_longitude):.2f} degrees.")
print(f"Jupiter is {float(jupiter_sign_degrees)
      :.2f} degrees in {jupiter_sign}.")
print(f"Jupiter is in the Bound of {jupiter_bound}")
print(f"Jupiter is in the Decan of {jupiter_decan}")

print(f"\nNotes on Jupiter's dignity: ")

if jupiter_in_domicile:
    print(f"Jupiter is in its own Domicile.")

if jupiter_in_exaltation:
    print(f"Jupiter is in its own sign of Exaltation.")

if jupiter_is_super_exalted:
    print(f"Jupiter is in its super Exaltation degrees.")

if jupiter_in_triplicity:
    print(f"Jupiter is in its own Triplicity sign.")

if jupiter_bound == 'Jupiter':
    print(f"Jupiter is in its own Bound")

if jupiter_decan == 'Jupiter':
    print(f"Jupiter is in its own Decan")

if jupiter_in_detriment:
    print(f"Jupiter is in its Detriment")

if jupiter_in_fall:
    print(f"Jupiter is in its own Fall.")

if not any([jupiter_in_domicile, jupiter_in_exaltation, jupiter_is_super_exalted,
            jupiter_in_triplicity, jupiter_bound == 'Jupiter', jupiter_decan == 'Jupiter',
            jupiter_in_detriment, jupiter_in_fall]):
    print(f"Jupiter is Peregrine")

print(f"\nSaturn ♄")
print(f"Saturn's ecliptic longitude: {float(saturn_longitude):.2f} degrees.")
print(f"Saturn is {float(saturn_sign_degrees):.2f} degrees in {saturn_sign}.")
print(f"Saturn is in the bound of {saturn_bound}")
print(f"Saturn is in the decan of {saturn_decan}")

print(f"\nNotes on Saturn's dignity: ")

if saturn_in_domicile:
    print(f"Saturn is in its own Domicile.")

if saturn_in_exaltation:
    print(f"Saturn is in its own sign of Exaltation.")

if saturn_is_super_exalted:
    print(f"Saturn is in its super Exaltation degrees.")

if saturn_in_triplicity:
    print(f"Saturn is in its own Triplicity sign.")

if saturn_bound == 'Saturn':
    print(f"Saturn is in its own Bound")

if saturn_decan == 'Saturn':
    print(f"Saturn is in its own Decan")

if saturn_in_detriment:
    print(f"Saturn is in its Detriment")

if saturn_in_fall:
    print(f"Saturn is in its own Fall.")

if not any([saturn_in_domicile, saturn_in_exaltation, saturn_is_super_exalted,
            saturn_in_triplicity, saturn_bound == 'Saturn', saturn_decan == 'Saturn',
            saturn_in_detriment, saturn_in_fall]):
    print(f"Saturn is Peregrine")


print(
    f"\nThe degree of the Ascendant is: {float(ascendant_longitude):.2f}"
    f"\nThe Ascendant is {float(ascendant_sign_degrees):.2f} degrees in {
        ascendant_sign}."
)

# test
print(
    f"\nYour selected house system: {selected_house_system}."
    f"\n{house_cusps}"
)
