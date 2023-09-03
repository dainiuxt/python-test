def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
  for_possible_change = not_working_street_lights
  working_neighbour_illuminations = [1.0,
                                    0.9471929492141141,
                                    0.8049220530197625,
                                    0.613685849032916,
                                    0.41977377692101514,
                                    0.257609226691527,
                                    0.14183533411213797,
                                    0.07006229694981106,
                                    0.031049972484260627,
                                    0.012345679012345678]

  # Making a list of WORKING street lights for calculation check
  working_street_lights = []
  distance = 0
  light_index = 0
  while distance <= road_length:
    if light_index in not_working_street_lights:
      light_index += 1
      distance += 20
    else:
      working_street_lights.append(light_index)
      light_index += 1
      distance += 20
  
  illuminations = [] # illuminations for not working street lights
  below_one_illuminations_index = [] #index of street lights where illumination < 1
  below_one_illuminations = []
  for val in not_working_street_lights:
    illumination = 0 # self illumination of not working street light
    for delta in range(-9, 10):
      calculate_number = val + delta
      if calculate_number in working_street_lights:
        illumination = illumination + working_neighbour_illuminations[abs(delta)]
    illuminations.append(illumination) # append street light illumination to the list
    if illumination < 1:
      below_one_illuminations_index.append(val) # index of very dimm (<1) street light
      below_one_illuminations.append(illumination) # values of very dimm (<1) street light      
  
  # At least every 7th street light should be working to have cumulative illumination above 1. We should check if len(below_one_illuminations) > 14 then replace every 7th lamp (remove every 7th member from list and check again), if list length < 14 we can simply remove the midle number. Downsides are that we can have 15 inactive lamps in a row, then some singles or 2-3, hence index consistency check should be implemented.
  
  print("Below 1 illuminations indexes:")
  print(below_one_illuminations_index)
  print("Below one illumination values:")
  print(below_one_illuminations)
  
  dimmest_set = []
  dimmest = illuminations.index(min(illuminations))
  dimmest_set.append(dimmest)
  return not_working_street_lights[dimmest_set[0]]




find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=[101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125])

# find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=[101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125])

if __name__ == "__main__":
    # This is an example test. When evaluating the task, more will be added:
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6]) == 5
    print("ALL TESTS PASSED")
    