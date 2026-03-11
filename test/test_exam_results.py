import csv
import datetime
import pytest as pt
from src.exam_results import ExamResult, read_exam_data
from pathlib import Path



invalid_result_data = [
    ({"student": "John Doe"}, KeyError),
    (
        {
            "student": "John Doe",
            "date": "1980-01-01",
            "exam": "Astronomy",
            "mood": "dead",
            "study_hours": "8",
            "sleep_hours": "2.5",
            "coffee_spent": "a lot"
        },
        ValueError
    )
]


def test_result_creation():
    data = {
        "student": "John Doe",
        "date": "1980-01-01",
        "exam": "Astronomy",
        "mood": "dead",
        "study_hours": "8",
        "sleep_hours": "2.5",
        "coffee_spent": "1000"
    }

    result = ExamResult.from_dict(data)
    assert result == ExamResult(
        student="John Doe",
        date=datetime.date(year=1980, month=1, day=1),
        exam="Astronomy",
        mood="dead",
        study_hours=8,
        sleep_hours=2.5,
        coffee_spent=1000
    )


@pt.mark.parametrize(
    "data,err",
    invalid_result_data
)
def test_invalid_result_creation(data, err):
    with pt.raises(err):
        ExamResult.from_dict(data)


def test_sorted():
    csvfile = Path("test/test_data.csv")
    results = read_exam_data([csvfile])

    with open(csvfile, "r") as file:
        reader = csv.DictReader(file)
        names = [elem["student"] for elem in reader]
        names.sort()

    assert names == [res.student for res in results]
