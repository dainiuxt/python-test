def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
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
  consecutives_below_one = []
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
  
  # ADDITIONAL TASK section starts here.
  # Logic: At least every 7th street light should be working to have cumulative illumination above 1. We should check if len(below_one_illuminations) > 14 then replace every 7th lamp (remove every 7th member from list and check again), if list length < 14 we can simply remove the midle number. Downsides are that we can have 15 inactive lamps in a row, then some singles or 2-3, hence index consistency check should be implemented.
  # Below code builds the list of consecutives list from non_working and illuminations_below_one (code borrowed from https://softhints.com/find-consecutive-numbers-in-a-list-in-python/, I chose vanilla python version at the end of article.)
  if len(below_one_illuminations) > 14:  
    current_consecutive = [below_one_illuminations_index[0]]
    for i in range(1, len(below_one_illuminations_index)):
      if below_one_illuminations_index[i] == below_one_illuminations_index[i-1] + 1:
          current_consecutive.append(below_one_illuminations_index[i])
      else:
          if len(current_consecutive) > 1:
              consecutives_below_one.append(current_consecutive)
          current_consecutive = [below_one_illuminations_index[i]]
    if len(current_consecutive) > 1:
      consecutives_below_one.append(current_consecutive)
  # END of borrowed code.

  # At least every 7th member of long inactive sequence should be replaced `len(consecutives_below_one[i])/7`, to keep illumination above 1.
  should_be_brightened = []
  for i in range(0, len(consecutives_below_one)):
    if len(consecutives_below_one[i]) > 7:
      j = 3
      while j < len(consecutives_below_one[i]):
        should_be_brightened.append(consecutives_below_one[i][j])
        j = j + 7

  # ADDITIONAL task code segment ENDS here. Outputs via `print()` will be provided below.
  
  dimmest_set = []
  if len(illuminations) != 0:
    dimmest = illuminations.index(min(illuminations))
    dimmest_set.append(dimmest)
  
  # print(f"Lamps on lightposts No. {should_be_brightened} should be changed to keep illumination at least 1.")
  # print(f"Total quantity of lamps should be changed to keep illumination at least 1: {len(should_be_brightened)}.")
  # print(f"The dimmest lamp for change is No. {not_working_street_lights[dimmest_set[0]]}")
  
  # Row below returns the dimmest lamp post index starting to count from 0 for testing.
  if len(dimmest_set) != 0:
    return not_working_street_lights[dimmest_set[0]]

find_index_of_darkest_street_light(road_length=200000, not_working_street_lights=[4, 5, 6, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217])

if __name__ == "__main__":
    # This is an example test. When evaluating the task, more will be added:
    print("1. Task test:")
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6]) == 5
    print("OK")
    
    print("2. Solution in the begining of the road:")
    assert find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=list(range(0, 500))) == 0
    print("OK")
    
    print("3. Solution in the end of the road:")
    assert find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=list(range(992, 1001))) == 1000
    print("OK")
    
    print("4. Discarded when reduced below 1%:")
    assert find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=list(range(988, 1001))) == 997
    print("OK")
    
    print("5. Solution in the first dark region:")
    assert find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=list(range(350, 365)) + list(range(600, 610))) == 357
    print("OK")
    
    print("6. Solution in the second dark region:")
    assert find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=list(range(350, 360)) + list(range(600, 615))) == 607
    print("OK")

    print("7. Solution in the last dark region:")
    assert find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=list(range(400, 410)) + list(range(422, 429)) + list(range(600, 615))) == 607
    print("OK")    

    print("8. Solution in the middle dark region:")
    assert find_index_of_darkest_street_light(road_length=20000, not_working_street_lights=[400, 401, 403, 420, 421, 422, 440, 441, 442]) == 421
    print("OK") 

    print("9. Solution for longest possible road:")
    assert find_index_of_darkest_street_light(road_length=2000000, not_working_street_lights=list(range(50000, 50016))) == 50007
    print("OK") 

    print("10. Solution for extralong road:")
    assert find_index_of_darkest_street_light(road_length=9000000, not_working_street_lights=list(range(50000, 50016))) == 50007
    print("OK") 

    print("11. Solution when road has only one lamp:")
    assert find_index_of_darkest_street_light(road_length=2000, not_working_street_lights=[0]) == 0
    print("OK") 

    print("12. Solution when all lamps are OK:")
    # print(find_index_of_darkest_street_light(road_length=2000, not_working_street_lights=[]))
    assert find_index_of_darkest_street_light(road_length=2000, not_working_street_lights=[]) == None
    print("OK") 
                    
    print("ALL TESTS PASSED")
