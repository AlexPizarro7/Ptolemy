# Ptolemy: An Horary Astrology Software

## Overview
Ptolemy is an evolving Python-based astrology software, currently in its development stage, with the ambition of becoming comprehensive and accessible software for those interested in the art of horary astrology.

Ptolemy aims to remain completely free and accessible to anyone. Unlike other traditional astrology software options, Ptolemy is focused on helping individuals not just visualize astrological charts but primarily analyze their data and understand the astrological principles of horary astrology in order to successfully interpret horary charts.

## Feautres
- **User-Friendly Input:** Simple interface for entering city, country, date, and time to generate a detailed astrological report.
- **GeoPy Integration:** Employs GeoPy for accurate geographical data input, enhancing location-based calculations.
- **Planetary Positions:** Leverages Swisseph to calculate precise planetary alignments for any given date and time.
- **Zodiac Sign, Bound, and Decan Determination** Utilizes the ecliptic longitude to calculate the sign, bound (term), and decan (face) each planet is in, providing foundational information for astrological interpretations.
- **Analysis of Essential Dignity** Assesses several astrological concepts to determine the essential dignity of each planet, such as domicile, exaltation, triplicity, detriment, fall, combust, cazimi, etc.

## Project Status: Work in Progress

### 🚧 Please Note 🚧
Ptolemy is currently a work in progress. This means:
- **Ongoing Development:** New features are actively being thought of and implemented.
- **Potential Bugs:** As with any project in its development phase, there might be bugs or unexpected behavior.
- **Open to Suggestions:** Feedback and ideas for new features or improvements are always welcome.

## Resources

The development of this astrology software has been informed and enriched by a variety of sources. These include both classical texts and modern online resources. Below is a list of key books and websites that have contributed to the knowledge base of this application:

### Books
- *Christian Astrology* by William Lilly
- *The Horary Textbook* by John Frawley
- *Ancient Astrology in Theory and Practice: A Manual of Traditional Techniques, Volume I: Assessing Planetary Condition* by Demetra George

### Websites
- [Astro.com AstroWiki](https://www.astro.com/astrowiki/en/Main_Page)

---

## Setup

- Clone the repository.
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment:
  - Windows: `.\venv\Scripts\activate`
  - macOS/Linux: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

