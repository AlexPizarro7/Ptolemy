
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


def is_planet_in_its_traditional_domicile(planet, planet_sign):
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

# def is_planet_in_its_detriment


def get_ptolemaic_bound_ruler(sign, degree):
    # Dictionary structure for Aries bounds. You'll need to extend this to other signs.
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
            (8, 15, 'Mercury')
            (15, 22, 'Jupiter')
            (22, 26, 'Saturn')
            (26, 30, 'Mars')
        ],
        'Gemini': [
            (0, 7, 'Mercury')
            (7, 14, 'Jupiter')
            (14, 21, 'Venus')
            (21, 25, 'Saturn')
            (25, 30, 'Mars')
        ],
        'Cancer': [
            (0, 6, 'Mars')
            (6, 13, 'Jupiter')
            (13, 20, 'Mercury')
            (20, 27, 'Venus')
            (27, 30, 'Saturn')
        ],
        'Leo': [
            (0, 6, 'Saturn')
            (6, 13, 'Mercury')
            (13, 19, 'Venus')
            (19, 25, 'Jupiter')
            (25, 30, 'Mars')
        ],
        'Virgo': [
            (0, 7, 'Mercury')
            (7, 13, 'Venus')
            (13, 18, 'Jupiter')
            (18, 24, 'Saturn')
            (24, 30, 'Mars')
        ],
        'Libra': [
            (0, 6, 'Saturn')
            (6, 11, 'Venus')
            (11, 19, 'Jupiter')
            (19, 24, 'Mercury')
            (24, 30, 'Mars')
        ],
        'Scorpio': [
            (0, 6, 'Mars')
            (6, 14, 'Jupiter')
            (14, 21, 'Venus')
            (21, 27, 'Mercury')
            (27, 30, 'Saturn')
        ],
        'Sagittarius': [
            (0, 8, 'Jupiter')
            (8, 14, 'Venus')
            (14, 19, 'Mercury')
            (19, 25, 'Saturn')
            (25, 30, 'Mars')
        ],
        'Capricorn': [
            (0, 6, 'Venus')
            (6, 12, 'Mercury')
            (12, 19, 'Jupiter')
            (19, 25, 'Mars')
            (25, 30, 'Saturn')
        ],
        'Aquarius': [
            (0, 6, 'Saturn')
            (6, 12, 'Mercury')
            (12, 20, 'Venus')
            (20, 25, 'Jupiter')
            (25, 30, 'Mars')
        ],
        'Pisces': [
            (0, 8, 'Venus')
            (8, 14, 'Jupiter')
            (14, 20, 'Mercury')
            (20, 26, 'Mars')
            (26, 30, 'Saturn')
        ]
        # Add other signs here...
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
    # Decans dictionary (Chaldean order)
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
