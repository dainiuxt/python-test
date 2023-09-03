### Task

There are street lights placed evenly every 20 meters on a straight road.
Most of the street lights are working and have the same illumination intencity.
Non-working street lights are provided as a list of their indexes.
If a street light is not working - its position can still be illuminated by neighboring lights.
Illumination is decreasing exponentially when the distance increases from a street light.
Please find an index of a street light, which has the lowest illumination. Its light bulb will be replaced.

Notes:
- The road lenght can be from 0 to 2000000m.
- The street lights are indexed from 0 and the first one stands at the begining of the road.
- The intensity of illumination can be calculated using `f(x) = 3^(-(x/90)^2)` formula, 
  where x is a distance from the street ligth in meters.
- If the street light is very far away and its illumination intencity is less than 0.01 - its illumination has to be ignored.
- In case there are several street lights with the same lowest illumination - provide the one with the lowest index.

Example:

```python
  road_length = 200
  non_working_street_lights = [4, 5, 6]
```

The length of the road is 200 meters and it has 11 street lights on it. Lights with indexes 4, 5 and 6 are not working.
The bulb of the street light with index 5 has to be replaced, because the illumination at it is the lowest.

Optional (for extra Karma points):
- Please find the minimal number of light bulbs, which is needed to be replaced
  to make cumulative illumination intencity at every street light non less than 1.


### My comments

Illumination for every street light is the sum of self illumination (1 if street light is working, 0 if street light is not working), plus illuminations of working neighbouring street lights.

Taking into account only thouse, which illuminations are greater than 0.01, we should use in calculations only thouse in distance of 180 m or index +/- 9. These illuminations can be calculated using function below (file `illuminations.py`):

 ```python 
  def calculate_illumination(length):
    distance = 0
    n = 0
    illuminations = []
    while distance <= length :
      illumination = 3**(-(distance/90)**2)
      if illumination > 0.01:
        illuminations.append(illumination)
        print(f"{n}: at {distance} meters with {round(illumination, 3)} illumination.")
        distance += 20
        n += 1
      else:
        break
    print(illuminations)
  calculate_illumination(2000)
```

Theese illuminations values are provided without rounding as a list in `main.py`.
