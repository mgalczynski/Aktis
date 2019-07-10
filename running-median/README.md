# Running median

## How to run

There is executable module [running_median](running_median.py) which requires one position argument - input file.
e.g.
To run program for third input set please execute:
```commandline
python -m running_median input03.txt
```

## How to run tests

This project use [pytest](https://docs.pytest.org/en/latest/) for testing, to install please execute:
```commandline
pip install -r requirements-dev.txt
```
Then to run all test in this project please execute:
```commandline
python -m pytest
``` 