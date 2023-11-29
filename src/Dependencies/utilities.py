# Imports for Geopy
from geopy.geocoders import Nominatim
import swisseph as swis_eph
from datetime import datetime, timezone, timedelta
from timezonefinder import TimezoneFinder
import pytz


# This function returns the coordinates of a specified city and country


def get_coordinates(city, country):
    """
    Calculates the latitude and longitude for a specified city and country using Nominatim.

    Parameters:
    - city (str): The city's name.
    - country (str): The country's name.

    Returns:
    - list: A list of namedtuples or None. Each namedtuple contains attributes like latitude,
            longitude, and address. If no matches are found, returns None.
    """
    geolocator = Nominatim(user_agent="AstrologyAppProject")
    locations = geolocator.geocode(f"{city}, {country}", exactly_one=False)
    return locations


def calculate_current_julian_day():
    """
    Calculates the current Julian Day Number (JDN) based on the UTC time.

    Returns:
    - tuple: A tuple containing the Julian Day Number and the current datetime object in UTC.
             The JDN is a floating-point number that represents the number of days since
             January 1, 4713 BCE at noon UTC. JDN (jd) is used as a parameter for many other functions in this software 
    """
    # Retrieves current date and time in UTC
    now = datetime.now(timezone.utc)

    # Extract individual components from the 'now' datetime object
    year, month, day, hour, minute, second = now.year, now.month, now.day, now.hour, now.minute, now.second

    # Converts UTC time to decimal format
    ut = hour + minute/60.0 + second/3600.0
    # Converts date and time to Julian day
    jd = swis_eph.julday(year, month, day, ut)

    return jd, now


def calculate_custom_julian_day(year, month, day, hour, minute, am_pm, lat, lon):
    """
    Calculates the Julian Day Number (JDN) for a custom date and time, adjusted for a specific location's timezone.

    Parameters:
    - year (int): The year component of the date.
    - month (int): The month component of the date.
    - day (int): The day component of the date.
    - hour (int): The hour component of the time.
    - minute (int): The minute component of the time.
    - am_pm (str): A string indicating whether the time is 'AM' or 'PM'.
    - lat (float): The latitude of the location.
    - lon (float): The longitude of the location.

    Returns:
    - float: The Julian Day Number representing the given date and time in UTC.
    """

    if am_pm == "PM" and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12:
        hour = 0

    # Create a naive datetime object
    custom_datetime = datetime(year, month, day, hour, minute)

    # Find the timezone of the given location
    tf = TimezoneFinder()
    tz_str = tf.timezone_at(lat=lat, lng=lon)  # Get the timezone string
    if tz_str is None:
        raise ValueError(
            f"Could not determine the timezone for the location: {lat}, {lon}")

    # Use the timezone string to get a timezone object
    timezone_location = pytz.timezone(tz_str)

    # Make the datetime object timezone aware
    custom_datetime = timezone_location.localize(custom_datetime)

    # Convert the timezone aware datetime to UTC
    custom_datetime_utc = custom_datetime.astimezone(pytz.utc)

    # Use the adjusted hour value directly
    ut = custom_datetime_utc.hour + custom_datetime_utc.minute / 60.0

    jd = swis_eph.julday(custom_datetime_utc.year,
                         custom_datetime_utc.month, custom_datetime_utc.day, ut)

    return jd, custom_datetime_utc


def calculate_ecliptic_longitude(planet_name, jd, location_latitude, location_longitude):
    """
    Calculates the ecliptic longitude of a specified planet for a given Julian Day (JD).

    Parameters:
    - planet_name (str): Name of the planet (e.g., 'Sun', 'Moon', 'Mars').
    - jd (float): Julian Day for which to perform the calculation.
    - location_latitude (float): Geographic latitude of the observation point in degrees.
    - location_longitude (float): Geographic longitude of the observation point in degrees.

    Returns:
    - float: Ecliptic longitude of the planet in degrees.
    """

    PLANETS = {
        'Sun': swis_eph.SUN,
        'Moon': swis_eph.MOON,
        'Mercury': swis_eph.MERCURY,
        'Venus': swis_eph.VENUS,
        'Mars': swis_eph.MARS,
        'Jupiter': swis_eph.JUPITER,
        'Saturn': swis_eph.SATURN,
        'Uranus': swis_eph.URANUS,
        'Neptune': swis_eph.NEPTUNE,
        'Pluto': swis_eph.PLUTO
    }

    if planet_name not in PLANETS:
        raise ValueError(f"'{planet_name}' is not a recognized planet.")

    planet_id = PLANETS[planet_name]

    # Set the topocentric flag and location
    flag = swis_eph.FLG_TOPOCTR
    swis_eph.set_topo(location_longitude, location_latitude, 0)
    xx, _ = swis_eph.calc_ut(jd, planet_id, flag)

    ecliptic_longitude = xx[0]

    return ecliptic_longitude


def get_sign_degrees(ecliptic_longitude):
    """
    Calculates the degree within a zodiac sign for a given ecliptic longitude.

    This function determines the specific degree within a zodiac sign that corresponds
    to the ecliptic longitude of a planet. The ecliptic longitude is measured in degrees.

    Parameters:
    - ecliptic_longitude (float): The ecliptic longitude of the planet, in degrees.

    Returns:
    - float: The degree within the corresponding zodiac sign.

    Raises:
    - ValueError: If the ecliptic longitude is less than 0, greater than or equal to 360, 
                  or a non-numeric value.

    Examples:
    >>> get_sign_degrees(31.59)
    1.59

    >>> get_sign_degrees(360)
    ValueError: Invalid ecliptic longitude
    """

    zodiac_signs = [
        ("Aries", 0, 30),
        ("Taurus", 30, 60),
        ("Gemini", 60, 90),
        ("Cancer", 90, 120),
        ("Leo", 120, 150),
        ("Virgo", 150, 180),
        ("Libra", 180, 210),
        ("Scorpio", 210, 240),
        ("Sagittarius", 240, 270),
        ("Capricorn", 270, 300),
        ("Aquarius", 300, 330),
        ("Pisces", 330, 360)
    ]

    # Normalize ecliptic longitude if it is 360 degrees
    if ecliptic_longitude >= 360:
        ecliptic_longitude %= 360

    # Find the zodiac sign and calculate the degree within that sign
    for sign, start, end in zodiac_signs:
        if start <= ecliptic_longitude < end:
            return ecliptic_longitude - start

    # Handle invalid longitude values
    raise ValueError("Invalid ecliptic longitude")


def get_zodiac_sign(ecliptic_longitude):
    """
    Determines the zodiac sign corresponding to a given ecliptic longitude.

    Parameters:
    - ecliptic_longitude (float): The ecliptic longitude in degrees.

    Returns:
    - str: The name of the zodiac sign that corresponds to the given ecliptic longitude.
    """
    zodiac_signs = [
        ("Aries", 0, 30),
        ("Taurus", 30, 60),
        ("Gemini", 60, 90),
        ("Cancer", 90, 120),
        ("Leo", 120, 150),
        ("Virgo", 150, 180),
        ("Libra", 180, 210),
        ("Scorpio", 210, 240),
        ("Sagittarius", 240, 270),
        ("Capricorn", 270, 300),
        ("Aquarius", 300, 330),
        ("Pisces", 330, 360)
    ]

    # Normalize the ecliptic longitude to the range [0, 360)
    ecliptic_longitude %= 360

    # Find the zodiac sign corresponding to the ecliptic longitude
    for sign, start_degree, end_degree in zodiac_signs:
        if start_degree <= ecliptic_longitude < end_degree:
            return sign


def get_house_system_code(house_system_name):
    """
    Converts a house system name to the corresponding Swiss Ephemeris code.
    For simplicity, many functions in this software need the Swiss Ephemeris code
    as a paramater, rather than the house system name directy.

    Args:
        house_system_name (str): The name of the house system.

    Returns:
        str: The corresponding Swiss Ephemeris code for the house system.
    """
    house_system_codes = {
        'Placidus': 'P',
        'Whole Sign': 'W',
        'Regiomontanus': 'R',
        'Koch': 'K',
        'Porphyry': 'O',
        'Equal (MC)': 'E',
        'Axial Rotation': 'X',
        'Horizontal System': 'H',
        # Add any other house systems and their codes as needed
    }

    # Retrieve the house system code or raise an error if not found
    code = house_system_codes.get(house_system_name)
    if not code:
        raise ValueError(f"Unsupported house system: {house_system_name}")
    return code


def calculate_ascendant(jd, location_latitude, location_longitude, house_system_code):
    """
    Calculates the Ascendant degrees for a given Julian Day and location.

    Parameters:
    - jd (float): The Julian Day for the calculation.
    - location_latitude (float): The latitude of the location.
    - location_longitude (float): The longitude of the location.
    - house_system_code (str): The code for the house system to use.

    Returns:
    - float: The ecliptic longitude of the Ascendant in degrees.
    """
    # Calculate the houses using the Swiss Ephemeris library
    cusps, ascmc = swis_eph.houses(
        jd, location_latitude, location_longitude, house_system_code.encode('utf-8'))

    # The Ascendant is the first house cusp in most house systems
    # Ascendant is always the first element in the ascmc array
    ascendant = ascmc[0]

    return ascendant


def calculate_midheaven(jd, location_latitude, location_longitude, house_system_code):
    """
    Calculates the Midheaven (Medium Coeli, MC) for a given Julian Day and location.

    Parameters:
    - jd (float): The Julian Day for the calculation.
    - location_latitude (float): The latitude of the location.
    - location_longitude (float): The longitude of the location.
    - house_system_code (str): The code for the house system to use.

    Returns:
    - float: The ecliptic longitude of the Midheaven in degrees.
    """
    # Calculate the houses using the Swiss Ephemeris library
    cusps, ascmc = swis_eph.houses(
        jd, location_latitude, location_longitude, house_system_code.encode('utf-8'))

    # The Midheaven (MC) is the second element in the ascmc array
    midheaven = ascmc[1]

    return midheaven


def calculate_descendant(jd, location_latitude, location_longitude, house_system_code):
    """
    Calculates the Descendant for a given Julian Day and location.

    Parameters:
    - jd (float): The Julian Day for the calculation.
    - location_latitude (float): The latitude of the location.
    - location_longitude (float): The longitude of the location.
    - house_system_code (str): The code for the house system to use.

    Returns:
    - float: The ecliptic longitude of the Descendant in degrees.
    """
    # Calculate the houses using the Swiss Ephemeris library
    cusps, ascmc = swis_eph.houses(
        jd, location_latitude, location_longitude, house_system_code.encode('utf-8'))

    # The Ascendant (ASC) is the first element in the ascmc array
    ascendant = ascmc[0]

    # The Descendant (DC) is 180 degrees opposite the Ascendant
    descendant = (ascendant + 180) % 360

    return descendant


def calculate_ic(jd, location_latitude, location_longitude, house_system_code):
    """
    Calculates the Imum Coeli (IC) for a given Julian Day and location.

    Parameters:
    - jd (float): The Julian Day for the calculation.
    - location_latitude (float): The latitude of the location.
    - location_longitude (float): The longitude of the location.
    - house_system_code (str): The code for the house system to use.

    Returns:
    - float: The ecliptic longitude of the Imum Coeli in degrees.
    """
    # Calculate the houses using the Swiss Ephemeris library
    cusps, ascmc = swis_eph.houses(
        jd, location_latitude, location_longitude, house_system_code.encode('utf-8'))

    # The Midheaven (MC) is the second element in the ascmc array
    midheaven = ascmc[1]

    # The IC (Imum Coeli) is 180 degrees opposite the Midheaven
    ic = (midheaven + 180) % 360

    return ic


def calculate_house_cusps(jd, location_latitude, location_longitude, house_system_code):
    """
    Calculate the cusps of the twelve astrological houses based on the given parameters.

    Args:
        jd (float): Julian Day.
        location_latitude (float): Latitude of the location.
        location_longitude (float): Longitude of the location.
        house_system_code (str): Code of the house system to use.

    Returns:
        list: A list of floats representing the ecliptic longitudes of the twelve house cusps, including the Ascendant.
    """
    cusps, ascmc = swis_eph.houses(
        jd, location_latitude, location_longitude, house_system_code.encode('utf-8'))
    # The first value in the cusps array is the Ascendant, which is also the cusp of the first house
    return cusps
