import matplotlib.pyplot as plt
import numpy as np


def draw_astro_chart(planet_longitudes, ascendant_degree, house_cusps):
    planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
    symbols = ['☉', '☽', '☿', '♀', '♂', '♃', '♄']

    # Adjusting the degrees based on the ascendant
    adjusted_degrees = {planet: (long - ascendant_degree) %
                        360 for planet, long in planet_longitudes.items()}

    # Creating the astrological chart
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Drawing houses
    for cusp in house_cusps:
        ax.axvline(np.radians(cusp - ascendant_degree),
                   color='grey', linewidth=0.5)

    # Placing planets
    for i, planet in enumerate(planets):
        location = np.radians(adjusted_degrees[planet])
        ax.plot(location, 1, marker='o', markersize=5,
                label=f"{planet} {symbols[i]}")
        ax.text(location, 1.1, symbols[i], horizontalalignment='center',
                size=20, color='black', weight='semibold')

    ax.set_rticks([])  # Removing radial ticks
    ax.set_yticklabels([])
    ax.spines['polar'].set_visible(False)  # Removing the circular spine
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))
    plt.show()


# Example data
planet_longitudes = {
    "Sun": 148.01,
    "Moon": 264.06,
    "Mercury": 131.46,
    "Venus": 146.42,
    "Mars": 232.54,
    "Jupiter": 34.97,
    "Saturn": 47.12
}

ascendant_degree = 140.40038430992215
house_cusps = [120.0, 150.0, 180.0, 210.0, 240.0,
               270.0, 300.0, 330.0, 0.0, 30.0, 60.0, 90.0]

# Calling the function
draw_astro_chart(planet_longitudes, ascendant_degree, house_cusps)
