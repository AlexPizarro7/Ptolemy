

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


def is_day_chart(sun_longitude, ascendant_longitude):
    """
    Determines if an astrological chart is a day chart or a night chart based on the Sun's position relative to the Ascendant. A chart is considered a day chart if the Sun is above the horizon, which means its ecliptic longitude is between the Ascendant's longitude and the Descendant's longitude

    Parameters:
    - sun_longitude (float): The ecliptic longitude of the Sun, measured in degrees (0-359.99).
    - ascendant_longitude (float): The ecliptic longitude of the Ascendant, measured in degrees (0-359.99).

    Returns:
    - bool: True if the chart is a day chart (Sun above the horizon), False if the chart is a night chart (Sun below the horizon).
    """
    # Calculate Descendant's longitude
    descendant_longitude = (ascendant_longitude + 180) % 360

    # Check if Sun is between Ascendant and Descendant
    if ascendant_longitude < descendant_longitude:
        return ascendant_longitude <= sun_longitude < descendant_longitude
    else:
        return sun_longitude < descendant_longitude or sun_longitude >= ascendant_longitude


def get_ptolemaic_bound_ruler(sign, degree):
    """
    This function determines the ruler of the bound that a planet is in based on the provided sign and degree. This function uses the Ptolemaic system for bound definitions

    Parameters:
    - sign (str): The zodiac sign (e.g., 'Aries', 'Taurus', etc.).
    - degree (int): The degree within the sign (0-29).

    Returns:
    - str: The name of the planet that rules the bound for the given sign and degree. 
         Returns "Invalid sign or degree" if the sign is not found or if the degree is out of the specified bounds.

    Note:
    The bounds are defined based on the Ptolemaic system and vary for each sign. 
    """
    bounds = {
        'Aries': [
            (0, 6, 'Jupiter'),
            (6, 14, 'Venus'),
            (14, 21, 'Mercury'),
            (21, 26, 'Mars'),
            (26, 30, 'Saturn')
        ],
        'Taurus': [
            (0, 8, 'Venus'),
            (8, 15, 'Mercury'),
            (15, 22, 'Jupiter'),
            (22, 26, 'Saturn'),
            (26, 30, 'Mars'),
        ],
        'Gemini': [
            (0, 7, 'Mercury'),
            (7, 14, 'Jupiter'),
            (14, 21, 'Venus'),
            (21, 25, 'Saturn'),
            (25, 30, 'Mars'),
        ],
        'Cancer': [
            (0, 6, 'Mars'),
            (6, 13, 'Jupiter'),
            (13, 20, 'Mercury'),
            (20, 27, 'Venus'),
            (27, 30, 'Saturn'),
        ],
        'Leo': [
            (0, 6, 'Saturn'),
            (6, 13, 'Mercury'),
            (13, 19, 'Venus'),
            (19, 25, 'Jupiter'),
            (25, 30, 'Mars'),
        ],
        'Virgo': [
            (0, 7, 'Mercury'),
            (7, 13, 'Venus'),
            (13, 18, 'Jupiter'),
            (18, 24, 'Saturn'),
            (24, 30, 'Mars'),
        ],
        'Libra': [
            (0, 6, 'Saturn'),
            (6, 11, 'Venus'),
            (11, 19, 'Jupiter'),
            (19, 24, 'Mercury'),
            (24, 30, 'Mars'),
        ],
        'Scorpio': [
            (0, 6, 'Mars'),
            (6, 14, 'Jupiter'),
            (14, 21, 'Venus'),
            (21, 27, 'Mercury'),
            (27, 30, 'Saturn'),
        ],
        'Sagittarius': [
            (0, 8, 'Jupiter'),
            (8, 14, 'Venus'),
            (14, 19, 'Mercury'),
            (19, 25, 'Saturn'),
            (25, 30, 'Mars'),
        ],
        'Capricorn': [
            (0, 6, 'Venus'),
            (6, 12, 'Mercury'),
            (12, 19, 'Jupiter'),
            (19, 25, 'Mars'),
            (25, 30, 'Saturn'),
        ],
        'Aquarius': [
            (0, 6, 'Saturn'),
            (6, 12, 'Mercury'),
            (12, 20, 'Venus'),
            (20, 25, 'Jupiter'),
            (25, 30, 'Mars'),
        ],
        'Pisces': [
            (0, 8, 'Venus'),
            (8, 14, 'Jupiter'),
            (14, 20, 'Mercury'),
            (20, 26, 'Mars'),
            (26, 30, 'Saturn'),
        ]
    }

    # Check if the sign is in the dictionary
    if sign in bounds:
        # Iterate over the bounds for the given sign
        for lower_bound, upper_bound, ruler in bounds[sign]:
            if lower_bound <= degree < upper_bound:
                return ruler

    # If the sign is not found or degree is out of bounds, return an error message
    return "Invalid sign or degree"


def get_traditional_decan(sign, sign_degrees):
    """
    This function identifies the ruling planet of the decan for in which a planet is currently in, given the sign in question and the sign degrees the planet is in. This function uses the Chaldean order system, which is used in tradtional astrology. 

    Parameters:
    - sign (str): The zodiac sign (e.g., 'Aries', 'Taurus', etc.).
    - sign_degrees (int): The degree within the sign (0-29).

    Returns:
    - str: The name of the planet ruling the decan of the given sign and degree.
    Returns None if the sign is not recognized or if the degree is out of bounds.
    """

    decans = {
        'Aries': [('Mars', 0, 10), ('Sun', 10, 20), ('Venus', 20, 30)],
        'Taurus': [('Mercury', 0, 10), ('Moon', 10, 20), ('Saturn', 20, 30)],
        'Gemini': [('Jupiter', 0, 10), ('Mars', 10, 20), ('Sun', 20, 30)],
        'Cancer': [('Venus', 0, 10), ('Mercury', 10, 20), ('Moon', 20, 30)],
        'Leo': [('Saturn', 0, 10), ('Jupiter', 10, 20), ('Mars', 20, 30)],
        'Virgo': [('Sun', 0, 10), ('Venus', 10, 20), ('Mercury', 20, 30)],
        'Libra': [('Moon', 0, 10), ('Saturn', 10, 20), ('Jupiter', 20, 30)],
        'Scorpio': [('Mars', 0, 10), ('Sun', 10, 20), ('Venus', 20, 30)],
        'Sagittarius': [('Mercury', 0, 10), ('Moon', 10, 20), ('Saturn', 20, 30)],
        'Capricorn': [('Jupiter', 0, 10), ('Mars', 10, 20), ('Sun', 20, 30)],
        'Aquarius': [('Venus', 0, 10), ('Mercury', 10, 20), ('Moon', 20, 30)],
        'Pisces': [('Saturn', 0, 10), ('Jupiter', 10, 20), ('Mars', 20, 30)]
    }

    for ruler, start, end in decans.get(sign, []):
        if start <= sign_degrees < end:
            return ruler  # Returning only the ruler of the decan
    return None


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
