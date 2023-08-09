from ooad.chapter_10.subway.connection import Connection
from ooad.chapter_10.subway.station import Station


class Subway:
    __stations: list[Station]
    __connections: list[Connection]
    __network: dict[Station, list[Station]] = {}

    def __init__(self) -> None:
        self.__stations = []
        self.__connections = []

    def add_station(self, station_name: str) -> None:
        if not self.has_station(station_name):
            self.__stations.append(Station(station_name))

    def has_station(self, station_name: str) -> bool:
        return Station(station_name) in self.__stations

    def has_connection(self, station1_name: str, station2_name: str, line_name: str) -> bool:
        station1 = Station(station1_name)
        station2 = Station(station2_name)
        for connection in self.__connections:
            if (
                connection.get_line_name().lower() == line_name.lower()
                and connection.get_station1() == station1
                and connection.get_station2() == station2
            ):
                return True

        return False

    def add_connection(self, station1_name: str, station2_name: str, line_name: str) -> Connection:
        if self.has_station(station1_name) and self.has_station(station2_name):
            station1 = Station(station1_name)
            station2 = Station(station2_name)
            connection = Connection(station1, station2, line_name)
            self.__connections.append(connection)
            self.__connections.append(Connection(station2, station1, line_name))
            self.__add_to_network(station1, station2)
            self.__add_to_network(station2, station1)
            return connection
        else:
            raise ValueError("Invalid connection!")

    def get_directions(self, start_station_name: str, end_station_name: str) -> list[Connection]:
        if not self.has_station(start_station_name) or not self.has_station(end_station_name):
            raise ValueError("Stations entered do not exist on this subway.")

        start = Station(start_station_name)
        end = Station(end_station_name)
        route: list[Connection] = []
        reachable_stations: list[Station] = []
        previous_stations: dict[Station, Station] = {}

        # Start by getting all neighboring stations of the start station. If end station is a
        # neighbor of the start station, we have a direct route
        neighbors = self.__network[start]
        for station in neighbors:
            if station == end:
                route.append(self.__get_connection(start, end))
                return route

            reachable_stations.append(station)
            previous_stations[station] = start

        next_stations = list(neighbors)
        current_station = start

        search_loop = False
        # Go through all the stations we know, trying to find a route to the end station
        for _ in range(1, len(self.__stations)):
            tmp_next_stations = []

            # For each neighboring station
            for station in next_stations:
                reachable_stations.append(station)
                current_station = station

                # Get all neighboring stations of the current station
                current_neighbors = self.__network[current_station]

                # Check if one of the neighbors is our end station
                for neighbor in current_neighbors:
                    if neighbor == end:
                        reachable_stations.append(neighbor)
                        previous_stations[neighbor] = current_station
                        search_loop = True
                        break
                    elif neighbor not in reachable_stations:
                        reachable_stations.append(neighbor)
                        tmp_next_stations.append(neighbor)
                        previous_stations[neighbor] = current_station
                if search_loop:
                    break
            next_stations = tmp_next_stations

        # By this point, we've found the shortest path to the end station. Now, we'll backtrack
        # from the end station to the start station to construct the route
        key_station: Station = end
        while start != key_station:
            station = previous_stations[key_station]
            route.insert(0, self.__get_connection(station, key_station))
            key_station = station

        return route

    def __get_connection(self, station1: Station, station2: Station) -> Connection:
        for connection in self.__connections:
            one = connection.get_station1()
            two = connection.get_station2()

            if station1 == one and station2 == two:
                return connection

        raise ValueError

    def __add_to_network(self, station1: Station, station2: Station) -> None:
        connecting_stations: list[Station]
        if station1 in self.__network:
            connecting_stations = self.__network[station1]
            if station2 not in connecting_stations:
                connecting_stations.append(station2)
        else:
            connecting_stations = [station2]
            self.__network[station1] = connecting_stations
