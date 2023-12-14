# Imports for Geopy
from geopy.geocoders import Nominatim
import swisseph as swis_eph
from datetime import datetime, timezone, timedelta
from timezonefinder import TimezoneFinder
import pytz


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


def get_local_time_from_utc(utc_datetime, latitude, longitude):
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=latitude, lng=longitude)

    if timezone_str is None:
        print("Timezone could not be determined for the given location.")
        return utc_datetime  # Return the original UTC time if timezone not found

    timezone_obj = pytz.timezone(timezone_str)
    local_datetime = utc_datetime.astimezone(timezone_obj)
    return local_datetime


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
