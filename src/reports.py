import statistics
from itertools import groupby
from typing import Iterable
from tabulate import tabulate

from src.exam_results import ExamResult


class Reporter:
    def __init__(self):
        self.__report_types: dict[str, callable] = {
            "median-coffee": self.__median_coffee_report,
        }

    @property
    def report_types(self) -> list[str]:
        return list(self.__report_types.keys())

    def generate_report(self, typ: str, data: Iterable[ExamResult]) -> None:
        report_data, headers = self.__report_types[typ](data)
        tabulated = tabulate(
            report_data,
            headers=headers,
            tablefmt="github"
        )
        print(tabulated)

    @staticmethod
    def __median_coffee_report(data: Iterable[ExamResult]) -> tuple[list[tuple[str, int]], list[str]]:
        median_coffee: list[tuple[str, int]] = []

        grouped = groupby(data, key=lambda x: x.student)
        for name, exam_results in grouped:
            median = statistics.median(map(lambda x: x.coffee_spent, exam_results))
            median_coffee.append((name, median))

        median_coffee.sort(key=lambda x: x[1], reverse=True)
        return median_coffee, ["student", "median_coffee"]
