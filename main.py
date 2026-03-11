from src.cmdline_options import extract_cmdline_options, verify_options
from src.exam_results import read_exam_data

from src.reports import Reporter


def main() -> None:
    reporter = Reporter()
    options = extract_cmdline_options()
    verify_options(reporter.report_types, options)

    exam_data = read_exam_data(options.files)
    reporter.generate_report(options.report, exam_data)


if __name__ == "__main__":
    main()
