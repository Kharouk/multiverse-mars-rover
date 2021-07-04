from unittest import TestCase
from mars import update_coords, will_rover_leave_grid, move_rover


class TestUpdatingCoords(TestCase):
    def test_update_coords_north(self):
        coords = ["3", "4"]
        direction = "N"
        print(update_coords(coords, direction))
        assert update_coords(coords, direction) == [3, 5]

    def test_update_coords_south(self):
        coords = ["3", "4"]
        direction = "S"
        print(update_coords(coords, direction))
        assert update_coords(coords, direction) == [3, 3]

    def test_update_coords_east(self):
        coords = ["3", "4"]
        direction = "E"
        print(update_coords(coords, direction))
        assert update_coords(coords, direction) == [4, 4]

    def test_update_coords_west(self):
        coords = ["3", "4"]
        direction = "W"
        print(update_coords(coords, direction))
        assert update_coords(coords, direction) == [2, 4]


class TestRoverLeavingGrid(TestCase):
    def test_will_rover_leave_grid_true(self):
        grid = [1, 1]
        coords = [0, 1]
        direction = "N"
        assert will_rover_leave_grid(grid, coords, direction) is True

    def test_will_rover_leave_grid_false(self):
        grid = [4, 8]
        coords = [2, 2]
        direction = "N"
        assert will_rover_leave_grid(grid, coords, direction) is False


class TestControlRover(TestCase):
    def test_move_rover_north_than_right(self):
        grid_size = "4 8"
        expected = move_rover(grid_size, "FFFRFFFF", "N", ["0", "0"])
        assert expected == "4, 3 E"

    def test_move_rover_gets_list(self):
        grid_size = "4 8"
        expected = move_rover(grid_size, "FFLFRFF", "N", ["0", "2"])
        assert expected == "0, 4 W (Lost)"
