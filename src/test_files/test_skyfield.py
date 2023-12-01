# Topos - Allows you to specify a location on Earth by latitude and longitude

# Load - Used to load datasets, such as positions of planets
from skyfield.api import Topos, load
from datetime import datetime, timezone


# Creates Skyfield's own timescale, required
ts = load.timescale()
t = ts.now()

# Loads the JPL ephemeris DE421 (covers 1900-2050)
planets = load('de421.bsp')
# Extracts Mars and Earth data from planetary data
earth = planets['earth']
mars = planets['mars']

# From the prespective of earth, from this location specified by latitude and longitude, compute the position of Mars
astrometric = (earth + Topos(latitude_degrees=40.748817,
               longitude_degrees=-73.985428)).at(t).observe(mars)

# ecliptic_latlon() method returns the ecliptic latitude, longitude and the distance from Mars.
ecliptic_lat, ecliptic_lon, distance = astrometric.ecliptic_latlon()

# f-strings allow embedding expressions inside the string, curly brackets are used to enclose the expressions. 1f means number should have one decimal number, and the f means not in scientific notation.
print(
    f'\nMars has an ecliptic longitude of {ecliptic_lon.degrees:.1f} degrees and an ecliptic latitude of {ecliptic_lat.degrees:.1f} degrees.\n')

# Convert Skyfield Time to datetime python object in UTC
utc_dt = t.utc_datetime()

# Convert UTC datetime to local time
# utc_dt.replace(tzinfo=timezone.utc) - utc_dt is a naive (no timezone) object by default, we need to specify that its UTC
# .astimezone (tz=none) specifies conversion to no particular timezone, so it uses local by default
local_dt = utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

# Format the local datetime
formatted_time = local_dt.strftime('%Y-%m-%d %H:%M %Z')

print(
    f'\nThe date and time for this position in local time is {formatted_time}\n'
)
