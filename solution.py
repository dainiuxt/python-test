"""
TASK DEFINITION:

There are street lights placed evenly every 20 meters on a straight road.
Most of the street lights are working and have the same illumination intencity.
Non-working street lights are provided as a list of their indexes.
If a street light is not working - its position can still be illuminated by neighboring lights.
Illumination is decreasing exponentially when the distance increases from a street light.
Please find an index of a street light, which has the lowest illumination. Its light bulb will be replaced.
Notes:
- The road lenght can be from 0 to 2000000m.
- The street lights are indexed from 0 and the first one stands at the begining of the road.
- The intensity of illumination can be calculated using f(x) = 3^(-(x/90)^2) formula, 
  where x is a distance from the street ligth in meters.
- If the street light is very far away and its illumination intencity is less than 0.01 - its illumination has to be ignored.
- In case there are several street lights with the same lowest illumination - provide the one with the lowest index.
Example:
road_length = 200
non_working_street_lights = [4, 5, 6]
The length of the road is 200 meters and it has 11 street lights on it. Lights with indexes 4, 5 and 6 are not working.
The bulb of the street light with index 5 has to be replaced, because the illumination at it is the lowest.
Optional (for extra Karma points):
- Please find the minimal number of light bulbs, which is needed to be replaced
  to make cumulative illumination intencity at every street light non less than 1.
"""


# EXPECTED SOLUTION:

STEP = 20

def get_illumination(distance: int) -> float:
    return 3 ** (-((distance / 90) ** 2))

def get_number_of_relevant_neighbors_in_one_side() -> int:
    for i in range(1, 100):
        distance = i * STEP
        if get_illumination(distance) < 0.01:
            return i - 1
    return 100

NUMBER_OF_RELEVANT_NEIGHBORS = get_number_of_relevant_neighbors_in_one_side()


def find_index_of_darkest_street_light(
    road_length: int, not_working_street_lights: list[int]
) -> int:

    if 0 < road_length > 2000000:
        raise ValueError("Wrong road length")

    if not not_working_street_lights:
        raise ValueError("All street lights are working")

    NUMBER_OF_LIGHTS = road_length // 20 + 1

    min_index = 0
    min_illumination = float("inf")
    for not_working_index in not_working_street_lights:
        lowest_relevant_neighbor = max(
            0, not_working_index - NUMBER_OF_RELEVANT_NEIGHBORS
        )
        highest_relevant_neighbor = min(
            NUMBER_OF_LIGHTS - 1, not_working_index + NUMBER_OF_RELEVANT_NEIGHBORS
        )

        working_neighbor_indexes = [
            neighbor_index
            for neighbor_index in range(
                lowest_relevant_neighbor, highest_relevant_neighbor + 1
            )
            if neighbor_index not in not_working_street_lights
        ]

        cummulative_illumination = sum(
            get_illumination(abs(neighbor_index - not_working_index) * 20)
            for neighbor_index in working_neighbor_indexes
        )

        if min_illumination > cummulative_illumination:
            min_index = not_working_index
            min_illumination = cummulative_illumination

    return min_index


# TEST CASES USED TO EVALUATE THE SOLUTION:
from unittest import TestCase

class TestsFindIndexOfDarkestStreetLight(TestCase):
    def test_example_provided_in_the_task_definition(self):
        not_working_street_lights = [4, 5, 6]
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=200, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 5)

    def test_solution_is_in_the_beginning_of_the_road(self):
        not_working_street_lights = list(range(0, 500))
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=20000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 0)

    def test_solution_is_in_the_end_of_the_road(self):
        not_working_street_lights = list(range(992, 1001))
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=20000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 1000)

    def test_illumination_is_discarded_when_it_reduces_to_less_than_1_percent(self):
        not_working_street_lights = list(range(988, 1001))
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=20000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 997)

    def test_solution_detection_when_its_in_the_first_dark_region(self):
        not_working_street_lights = list(range(350, 365)) + list(range(600, 610))
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=20000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 357)

    def test_solution_detection_when_its_in_the_second_dark_region(self):
        not_working_street_lights = list(range(350, 360)) + list(range(600, 615))
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=20000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 607)

    def test_solution_detection_when_its_in_the_last_dark_region(self):
        not_working_street_lights = list(range(400, 410)) + list(range(422, 429)) + list(range(600, 615))
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=20000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 607)

    def test_illumination_is_lowest_in_the_middle_dark_region(self):
        not_working_street_lights = [400, 401, 403, 420, 421, 422, 440, 441, 442]
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=20000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 421)

    def test_the_road_is_longest_possible(self):
        not_working_street_lights = list(range(50000, 50016))
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=2000000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 50007)

    def test_road_is_longer_than_allowed(self):
        with self.assertRaises(Exception):
            not_working_street_lights = list(range(50000, 50016))
            darkest_street_light = find_index_of_darkest_street_light(
                road_length=9000000, not_working_street_lights=not_working_street_lights
            )

            # Note: Its fine if exception is not raised, if solution is not being searched for
            self.assertNotEqual(darkest_street_light, 50007)

    def test_road_has_only_one_light(self):
        not_working_street_lights = [0]
        darkest_street_light = find_index_of_darkest_street_light(
            road_length=0, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(darkest_street_light, 0)

    def test_all_lamps_are_working(self):
        with self.assertRaises(Exception):
            not_working_street_lights = []
            darkest_street_light = find_index_of_darkest_street_light(
                road_length=200, not_working_street_lights=not_working_street_lights
            )

            # Note: Its fine if exception is not raised, if solution is not being searched for
            self.assertIsNone(darkest_street_light)



# TEST CASE USED TO EVALUATE THE SOLUTION FOR OPTIONAL TASK:

class TestsCountMinimumNumberOfLightsToReplace(TestCase):
    def test_example_provided_in_the_task_definition(self):
        not_working_street_lights = list(range(20, 37))
        minimum_number_of_lights_to_be_replaced = count_minimum_number_of_lights_to_be_replaced(
            road_length=2000, not_working_street_lights=not_working_street_lights
        )
        self.assertEqual(minimum_number_of_lights_to_be_replaced, 2)
