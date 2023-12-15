
import swisseph as swis_eph


def is_planet_in_its_traditional_domicile(planet, planet_sign):
    """
    This function determines if a planet is in its own domicile, which is the sign(s) they are considered to have rulership over. This function uses the traditional rulership system since that is what horary astrology uses. 

    Parameters:
    - planet (str): The name of the planet (e.g., 'Sun', 'Moon', 'Mercury', etc.).
    - planet_sign (str): The zodiac sign that the planet is currently in (e.g., 'Aries', 'Taurus', etc.).

    Returns:
    bool: True if the planet is in its traditional domicile, False otherwise.
    """

    planet_rulerships = {
        'Sun': 'Leo',
        'Moon': 'Cancer',
        'Mercury': ['Gemini', 'Virgo'],
        'Venus': ['Taurus', 'Libra'],
        'Mars': ['Aries', 'Scorpio'],
        'Jupiter': ['Sagittarius', 'Pisces'],
        'Saturn': ['Capricorn', 'Aquarius'],
    }

    # Check if the sign is one of the ruling signs for the planet
    ruling_signs = planet_rulerships.get(planet)
    # If the planet rules multiple signs (Mercury, Venus, etc.)
    if isinstance(ruling_signs, list):
        return planet_sign in ruling_signs
    else:
        return planet_sign == ruling_signs


def is_planet_in_its_traditional_exaltation(planet, planet_sign):
    """
    This function checks if a given planet is currently in its exaltation sign, using the traditional rulership system.

    Parameters:
    - planet (str): The name of the planet (e.g., 'Sun', 'Moon', 'Mercury', etc.).
    - planet_sign (str): The zodiac sign that the planet is currently in (e.g., 'Aries', 'Taurus', etc.).

    Returns:
    bool: True if the planet is in its traditional exaltation sign, False otherwise.
    """
    planet_exaltations = {
        'Sun': 'Aries',
        'Moon': 'Taurus',
        'Mercury': 'Virgo',
        'Venus': 'Pisces',
        'Mars': 'Capricorn',
        'Jupiter': 'Cancer',
        'Saturn': 'Libra',
    }

    exaltation_sign = planet_exaltations.get(planet)
    return planet_sign == exaltation_sign


def is_planet_super_exalted(planet, planet_sign, planet_degree):
    """
    Determines if a planet is super exalted based on its sign and degree.

    Super exaltation is an astrological concept where a planet is not only in its exaltation sign but also in a specific degree within that sign, considered to be a position of utmost strength. This function checks if a given planet is in such a position.

    Parameters:
    - planet (str): The name of the planet (e.g., 'Sun', 'Moon', 'Mercury', etc.).
    - planet_sign (str): The zodiac sign that the planet is currently in.
    - planet_degree (float): The degree of the planet within its current sign. Fractional degrees are truncated to the nearest whole number for this calculation.

    Returns:
    - bool: True if the planet is super exalted (in both the correct sign and degree), False otherwise.
    """
    # Dictionary mapping planets to their exaltation sign and specific super exaltation degree
    planet_super_exaltations = {
        'Sun': ('Aries', 19),
        'Moon': ('Taurus', 3),
        'Mercury': ('Virgo', 15),
        'Venus': ('Pisces', 27),
        'Mars': ('Capricorn', 28),
        'Jupiter': ('Cancer', 15),
        'Saturn': ('Libra', 21),
        # Add other planets if necessary
    }

    exaltation_info = planet_super_exaltations.get(planet)
    if exaltation_info:
        exaltation_sign, super_exaltation_degree = exaltation_info
        # Truncate the planet_degree to get the integer part
        truncated_degree = int(planet_degree)
        return (planet_sign == exaltation_sign) and (truncated_degree == super_exaltation_degree)
    else:
        return False


def is_planet_in_its_triplicity(planet, sign, day_or_night_chart):
    """
    This function checks if a given planet is in the sign that it has triplicity rulership over under the given condition of it being in a day chart or night chart. This function uses the traditional rulership system. 

    Parameters:
    - planet (str): The name of the planet (e.g., 'Sun', 'Moon', 'Mercury', etc.).
    - sign (str): The zodiac sign to check for triplicity rulership (e.g., 'Aries', 'Taurus', etc.).
    - day_or_night_chart (bool): A boolean indicating the type of chart. True for a day chart, False for a night chart.

    Returns:
    - bool: True if the planet is the triplicity ruler of the sign under the given day/night condition, False otherwise.
    """

    triplicity_rulers = {
        'Aries': ('Sun', 'Jupiter'),
        'Taurus': ('Venus', 'Moon'),
        'Gemini': ('Saturn', 'Mercury'),
        'Cancer': ('Mars', 'Mars'),
        'Leo': ('Sun', 'Jupiter'),
        'Virgo': ('Venus', 'Moon'),
        'Libra': ('Saturn', 'Mercury'),
        'Scorpio': ('Mars', 'Mars'),
        'Sagittarius': ('Sun', 'Jupiter'),
        'Capricorn': ('Venus', 'Moon'),
        'Aquarius': ('Saturn', 'Mercury'),
        'Pisces': ('Mars', 'Mars'),
    }

    # Determine the appropriate ruler based on whether it's a day or night chart
    ruler = triplicity_rulers[sign][0] if day_or_night_chart else triplicity_rulers[sign][1]

    return planet == ruler


def is_planet_in_its_traditional_detriment(planet, planet_sign):
    """
    Determines if a planet is in its sign of detriment according to the traditional rulership system.

    Parameters:
    - planet (str): The name of the planet (e.g., 'Sun', 'Moon', 'Mercury', etc.). The function currently supports classical planets including the Sun and Moon.
    - planet_sign (str): The zodiac sign to check against the planet's detriment (e.g., 'Aries', 'Taurus', etc.).

    Returns:
    - bool: True if the planet is in its traditional detriment, False otherwise.
    """

    planet_detriments = {
        'Sun': 'Aquarius',
        'Moon': 'Capricorn',
        'Mercury': ['Sagittarius', 'Pisces'],
        'Venus': ['Aries', 'Scorpio'],
        'Mars': ['Taurus', 'Libra'],
        'Jupiter': ['Gemini', 'Virgo'],
        'Saturn': ['Cancer', 'Leo']
    }

    detriment_signs = planet_detriments.get(planet)
    if isinstance(detriment_signs, list):
        return planet_sign in detriment_signs
    else:
        return planet_sign == detriment_signs


def is_planet_in_its_traditional_fall(planet, planet_sign):
    """
    Determines if a planet is in its sign of fall according to the traditional rulership system. 

    Parameters:
    - planet (str): The name of the planet (e.g., 'Sun', 'Moon', 'Mercury', etc.).
    - planet_sign (str): The zodiac sign to check against the planet's fall (e.g., 'Aries', 'Taurus', etc.).

    Returns:
    - bool: True if the planet is in its traditional fall, False otherwise.
    """

    planet_falls = {
        'Sun': 'Libra',
        'Moon': 'Scorpio',
        'Mercury': 'Pisces',
        'Venus': 'Virgo',
        'Mars': 'Cancer',
        'Jupiter': 'Capricorn',
        'Saturn': 'Aries',
    }

    fall_sign = planet_falls.get(planet)
    return planet_sign == fall_sign


def is_planet_combust(planet_longitude, planet_sign, sun_longitude, sun_sign):
    """
    In horary astrology, a planet is considered combust when it is within 8.5 degrees of the Sun, and in the same zodiac sign as the sun. This function checks if a planet meets these conditions. 

    Parameters:
    - planet_longitude (float): The ecliptic longitude of the planet in degrees.
    - planet_sign (str): The zodiac sign in which the planet is located.
    - sun_longitude (float): The ecliptic longitude of the Sun in degrees.
    - sun_sign (str): The zodiac sign in which the Sun is located.

    Returns:
    - bool: True if the planet is combust, False otherwise.
    """

    # Check if the planet is in the same sign as the Sun
    if planet_sign != sun_sign:
        return False

    # Calculate the angular distance between the planet and the Sun
    angular_distance = abs(planet_longitude - sun_longitude)

    # Adjust for cases where the planet and the Sun are on opposite ends of the zodiac
    if angular_distance > 180:
        angular_distance = 360 - angular_distance

    # Check if the planet is within 8.5 degrees of the Sun
    return angular_distance < 8.5


def is_planet_cazimi(planet_longitude, planet_sign, sun_longitude, sun_sign):
    """
    In horary astrology, a planet is considered to be in cazimi when it is within 17.5 minutes (or 0.2916667 degrees) of the Sun's position. 

    Parameters:
    - planet_longitude (float): The ecliptic longitude of the planet in degrees.
    - planet_sign (str): The zodiac sign in which the planet is located.
    - sun_longitude (float): The ecliptic longitude of the Sun in degrees.
    - sun_sign (str): The zodiac sign in which the Sun is located.

    Returns:
    - bool: True if the planet is in cazimi, False otherwise.
    """

    # Check if the planet and the Sun are in the same zodiac sign
    if planet_sign != sun_sign:
        return False

    # Calculate the absolute difference in longitude
    longitude_difference = abs(planet_longitude - sun_longitude)

    # Check if the planet is within 0.2916667 degrees (17.5 minutes) of the Sun
    # Note that other sources say Cazimi is when the planet is within 1 degree of the Sun
    cazimi_threshold = 0.2916667
    return longitude_difference <= cazimi_threshold


def is_planet_in_retrograde(planet_name, jd, location_latitude, location_longitude):
    """
    In astrology, a planet is cosidered to be in retrograde when it appears to move 
    backwards in the sky. This function calculates the planet's position on two 
    consecutive days and checks if its ecliptic longitude decreases, indicating 
    retrograde motion.

    Parameters:
    - planet_name (str): Name of the planet (e.g., 'Mercury', 'Venus', 'Mars').
    - jd (float): Julian Day for the starting date of observation.
    - location_latitude (float): Geographic latitude of the observation point in degrees.
    - location_longitude (float): Geographic longitude of the observation point in degrees.

    Returns:
    - bool: True if the planet is in retrograde motion, False otherwise.
    """

    swis_eph.set_topo(location_longitude, location_latitude, 0)

    planets = {
        'Sun': swis_eph.SUN, 'Moon': swis_eph.MOON, 'Mercury': swis_eph.MERCURY,
        'Venus': swis_eph.VENUS, 'Mars': swis_eph.MARS, 'Jupiter': swis_eph.JUPITER,
        'Saturn': swis_eph.SATURN
    }

    planet = planets.get(planet_name)
    if planet is None:
        raise ValueError("Invalid planet name.")

    # Get the planet's position for the given Julian Day
    position1, _ = swis_eph.calc_ut(jd, planet)

    # Get the planet's position for the next day
    position2, _ = swis_eph.calc_ut(jd + 1, planet)

    # Determine if the planet is in retrograde
    return position1[0] > position2[0]
