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
