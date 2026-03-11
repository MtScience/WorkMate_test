import datetime
import pytest as pt

from src.exam_results import ExamResult
from src.reports import Reporter


exam_data = [
    ExamResult(
        student="John Doe",
        date=datetime.date(year=1980, month=1, day=1),
        exam="Astronomy",
        mood="dead",
        study_hours=8,
        sleep_hours=2.5,
        coffee_spent=1000
    ),
    ExamResult(
        student="Mark Smith",
        date=datetime.date(year=1980, month=1, day=2),
        exam="Computer Science",
        mood="dead",
        study_hours=8,
        sleep_hours=2.5,
        coffee_spent=700
    )
]

@pt.fixture
def reporter():
    reporter = Reporter()
    yield reporter
    del reporter


def test_median_coffee_report(reporter):
    report, headers = reporter._Reporter__median_coffee_report(exam_data)
    assert headers == ["student", "median_coffee"]
    assert report == [("John Doe", 1000), ("Mark Smith", 700)]


def test_invalid_report(reporter):
    report_type = "invalid_report"
    assert report_type not in reporter.report_types

    with pt.raises(KeyError):
        reporter.generate_report(report_type, exam_data)
