from typing import TextIO

from ooad.chapter_10.subway.connection import Connection


class SubwayPrinter:
    __out: TextIO

    def __init__(self, output_stream: TextIO) -> None:
        self.__out = output_stream

    def print_directions(self, route: list[Connection]) -> None:
        connection = route[0]
        current_line = connection.get_line_name()
        previous_line = current_line
        write_log: list[str] = []

        write_log.append(f"Start out at {connection.get_station1().get_name()}.\n")
        write_log.append(
            f"Get on the {current_line} heading towards {connection.get_station2().get_name()}.\n"
        )

        for i in range(1, len(route)):
            connection = route[i]
            current_line = connection.get_line_name()

            if current_line == previous_line:
                write_log.append(f"Continue past {connection.get_station1().get_name()}...\n")
            else:
                write_log.append(
                    f"When you get to {connection.get_station1().get_name()}, "
                    f"get off the {previous_line}.\n"
                )
                write_log.append(
                    f"Switch over to the {current_line}, heading towards "
                    f"{connection.get_station2().get_name()}.\n"
                )
                previous_line = current_line

        write_log.append(
            f"Get off at {connection.get_station2().get_name()} and enjoy yourself!\n"
        )

        for logline in write_log:
            self.__out.write(logline)
