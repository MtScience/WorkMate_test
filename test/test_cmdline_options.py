import pytest as pt

from src.cmdline_options import extract_cmdline_options, verify_options

missing_args = [
    ("--files test.csv".split(), "--report"),
    ("--report median-coffee".split(), "--files"),
]

allowed_types = ["median-coffee"]
invalid_args = [
    ("--files test.csv --report median-coffee".split(), "could not be found"),
    ("--files /home --report median-coffee".split(), "is not a file"),
    ("--files /test/test_data.csv --report mood".split(), "unknown report type"),
]


@pt.mark.parametrize(
    "args,required",
    missing_args
)
def test_missing_options(args, required):
    with pt.raises(SystemExit) as exc:
        extract_cmdline_options(args)
        assert f"the following arguments are required: {required}" in exc.value


@pt.mark.parametrize(
    "args,msg",
    invalid_args,
    ids=["missing file", "not a file", "invalid report type"]
)
def test_invalid_options(args, msg):
    options = extract_cmdline_options(args)
    with pt.raises(SystemExit) as exc:
        verify_options(allowed_types, options)
        assert msg in exc.value
