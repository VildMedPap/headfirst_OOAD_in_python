import io

import pytest
from ooad.chapter_10.loader.subway_loader import SubwayLoader
from ooad.chapter_10.printer.subway_printer import SubwayPrinter


class TestSubwayLoader:
    loader = SubwayLoader()
    objectville = loader.load_from_file("tests/chapter_10/ObjectvilleSubway.txt")
    buffer = io.StringIO()  # Creates an in-memory "file"

    def test_route_planner(self):
        # Given
        # An initiated Subway object, a buffer, and a desired start and stop station
        start_station_name = "Mighty Gumball, Inc."
        end_station_name = "Choc-O-Holic, Inc."

        # When
        # Getting the directions and printing the route to the buffer
        route = self.objectville.get_directions(start_station_name, end_station_name)
        printer = SubwayPrinter(self.buffer)
        printer.print_directions(route)

        # Seek back to the beginning of the buffer and read its content
        self.buffer.seek(0)
        actual = self.buffer.read()

        # Then
        # The output should be as expected
        expected = (
            f"Start out at {start_station_name}.\n"
            "Get on the Jacobson Line heading towards Servlet Springs.\n"
            "When you get to Servlet Springs, get off the Jacobson Line.\n"
            "Switch over to the Wirfs-Brock Line, heading towards Objectville Diner.\n"
            "Continue past Objectville Diner...\n"
            "When you get to Head First Lounge, get off the Wirfs-Brock Line.\n"
            "Switch over to the Gamma Line, heading towards OOA&D Oval.\n"
            "When you get to OOA&D Oval, get off the Gamma Line.\n"
            "Switch over to the Meyer Line, heading towards CSS Center.\n"
            "Continue past CSS Center...\n"
            "When you get to Head First Theater, get off the Meyer Line.\n"
            "Switch over to the Rumbaugh Line, heading towards Choc-O-Holic, Inc..\n"
            f"Get off at {end_station_name} and enjoy yourself!\n"
        )
        assert actual == expected
