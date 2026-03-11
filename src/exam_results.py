import csv
import datetime as dt

from dataclasses import dataclass
from pathlib import Path
from typing import Self, Iterable


@dataclass
class ExamResult:
    student: str
    exam: str
    date: dt.date
    coffee_spent: int
    sleep_hours: float
    study_hours: int
    mood: str

    @classmethod
    def from_dict(cls, csvdata: dict[str, str]) -> Self:
        return cls(
            student=csvdata["student"],
            exam=csvdata["exam"],
            date=dt.date.fromisoformat(csvdata["date"]),
            coffee_spent=int(csvdata["coffee_spent"]),
            sleep_hours=float(csvdata["sleep_hours"]),
            study_hours=int(csvdata["study_hours"]),
            mood=csvdata["mood"],
        )


def read_exam_data(files: Iterable[Path]) -> list[ExamResult]:
    results: list[ExamResult] = []
    for file in files:
        with open(file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            results.extend(map(ExamResult.from_dict, [result for result in reader]))

    results.sort(key=lambda x: x.student)
    return results
