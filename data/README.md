# Features in the fires.csv data
0. X: 
    - X-coordinate of the fire in the park
    - values: 1-9
1. Y:
    - Y-coordinate of the fire in the park
    - values: 2-9
2. month:
    - month in which the fire occurred
    - values: 'jan'-'dec'
3. day:
    - day on which the fire occurred
    - values: 'mon'-'sun'
4. FFMC:
    - the Fine Fuel Moisture Code index of the Fire Weather Index (FWI) system
    - values: 18.7-96.2
5. DMC:
    - the Duff Moisture Code index of the FWI system
    - values: 1.1-291.3
6. DC:
    - the Drought Code index of the FWI system
    - values: 7.9-860.6
7. ISI:
    - the Initial Spread Index of the FWI system
    - values: 0.0-56.1
8. temp:
    - temperature in degrees Celsius
    - values: 2.2-33.3
9. RH:
    - relative humidity in %
    - values: 15-100
10. wind:
    - wind velocity in km/h
    - values: 0.4-9.4
11. rain:
    - rainfall in mm/m^2
    - values: 0.0-6.4
12. area:
    - forest area that has been burnt in hectare
    - values: 0.09-1090.84

## According to https://www.nwcg.gov/publications/pms437/cffdrs/fire-weather-index-system :

### Fuel Moisture Codes:

**The Fine Fuel Moisture Code (FFMC)** represents fuel moisture of forest litter fuels under the shade of a forest canopy. It is intended to represent moisture conditions for shaded litter fuels, the equivalent of 16-hour timelag. It ranges from 0-101. Subtracting the FFMC value from 100 can provide an estimate for the equivalent (approximately 10h) fuel moisture content, most accurate when FFMC values are roughly above 80.

**The Duff Moisture Code (DMC)** represents fuel moisture of decomposed organic material underneath the litter. System designers suggest that it is represents moisture conditions for the equivalent of 15-day (or 360 hr) timelag fuels. It is unitless and open ended. It may provide insight to live fuel moisture stress.

**The Drought Code (DC)**, much like the Keetch-Byrum Drought Index, represents drying deep into the soil. It approximates moisture conditions for the equivalent of 53-day (1272 hour) timelag fuels. It is unitless, with a maximum value of 1000. Extreme drought conditions have produced DC values near 800.

### Fire Behaviour Indices:
**The Initial Spread Index (ISI)** is analogous to the NFDRS Spread Component (SC). It integrates fuel moisture for fine dead fuels and surface windspeed to estimate a spread potential. ISI is a key input for fire behavior predictions in the FBP system. It is unitless and open ended.