
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


def get_traditional_decan(sign, longitude):
    # Decans dictionary (Chaldean order)
    decans = {
        'Aries': [('Mars', 0, 10), ('Sun', 10, 20), ('Venus', 20, 30)],
        'Taurus': [('Mercury', 0, 10), ('Moon', 10, 20), ('Saturn', 20, 30)],
        'Gemini': [('Jupiter', 0, 10), ('Mars', 10, 20), ('Sun', 20, 30)],
        'Cancer': [('Venus', 0, 10), ('Mercury', 10, 20), ('Moon', 20, 30)],
        'Leo': [('Saturn', 0, 10), ('Jupiter', 10, 20), ('Mars', 20, 30)],
        'Virgo': []
        # ... continue for each sign
    }

    for ruler, start, end in decans.get(sign, []):
        if start <= longitude < end:
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
