import pytest
from ooad.chapter_10.loader.subway_loader import SubwayLoader


class TestSubwayLoader:
    loader = SubwayLoader()
    objectville = loader.load_from_file("tests/chapter_10/ObjectvilleSubway.txt")

    @pytest.mark.parametrize("station", ["DRY Drive", "Weather-O-Rama, Inc.", "Boards'R'Us"])
    def test_testing_has_stations(self, station):
        # Given
        # An initiated Subway object

        # When
        # Checking for having different stations with the has_station method

        # Then
        # It should return True
        assert self.objectville.has_station(station)

    @pytest.mark.parametrize(
        "station1,station2,line",
        [
            ("DRY Drive", "Head First Theater", "Meyer Line"),
            ("Weather-O-Rama, Inc.", "XHTML Expressway", "Wirfs-Brock Line"),
            ("Head First Theater", "Infinite Circle", "Rumbaugh Line"),
        ],
    )
    def test_testing_has_connctions(self, station1, station2, line):
        # Given
        # An initiated Subway object

        # When
        # Checking for having different connections with the has_connection method

        # Then
        # It should return True
        assert self.objectville.has_connection(station1, station2, line)
